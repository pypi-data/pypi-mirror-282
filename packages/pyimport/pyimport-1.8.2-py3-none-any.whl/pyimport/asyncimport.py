import _csv
import argparse
import logging
import asyncio
import os
import sys
import time
from asyncio import TaskGroup
from datetime import datetime, timezone

import aiofiles
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorCollection
from requests import exceptions
from asyncstdlib import enumerate as aenumerate

from pyimport import timer
from pyimport.importresult import ImportResults
from pyimport.csvreader import AsyncCSVReader
from pyimport.enricher import Enricher
from pyimport.fieldfile import FieldFileException, FieldFile
from pyimport.importcommand import ImportCommand
from pyimport.importresult import ImportResult
from pyimport.linereader import is_url, RemoteLineReader


class AsyncImportCommand(ImportCommand):

    def __init__(self, args=None):

        super().__init__(args)
        self._log = logging.getLogger(__name__)
        self._q = asyncio.Queue()

    @staticmethod
    def async_prep_collection(args):
        if args.writeconcern == 0:  # pymongo won't allow other args with w=0 even if they are false
            client = AsyncIOMotorClient(args.host, w=args.writeconcern)
        else:
            client = AsyncIOMotorClient(args.host, w=args.writeconcern, fsync=args.fsync, j=args.journal)

        database = client[args.database]
        collection = database[args.collection]

        return collection

    @staticmethod
    async def async_prep_import(args: argparse.Namespace, filename: str, field_info: FieldFile):
        collection = AsyncImportCommand.async_prep_collection(args)
        parser = ImportCommand.prep_parser(args, field_info, filename)

        if is_url(filename):
            csv_file = RemoteLineReader(url=filename)
        else:
            csv_file = await aiofiles.open(filename, "r")

        reader = AsyncCSVReader(file=csv_file,
                                limit=args.limit,
                                field_file=field_info,
                                has_header=args.hasheader,
                                delimiter=args.delimiter)

        return collection, reader, parser

    @staticmethod
    async def get_csv_doc(args, q, p: Enricher, async_reader: AsyncCSVReader):

        async for i, doc in aenumerate(async_reader, 1):
            if args.noenrich:
                d = doc
            else:
                d = p.enrich_doc(doc, i)
            await q.put(d)
        await q.put(None)
        return i

    @staticmethod
    async def put_db_doc(args, q, log, collection: AsyncIOMotorCollection, filename: str) -> ImportResult:
        buffer = []
        time_period = 1.0
        total_written = 0
        inserted_this_quantum = 0

        time_start = time.time()
        loop_timer = timer.Timer(start_now=True)
        while True:
            doc = await q.get()
            if doc is None:
                q.task_done()
                break
            else:
                buffer.append(doc)
                q.task_done()
                if len(buffer) == args.batchsize:
                    await collection.insert_many(buffer)
                    total_written = total_written + len(buffer)
                    inserted_this_quantum = inserted_this_quantum + len(buffer)
                    buffer = []
                    elapsed = loop_timer.elapsed()
                    if elapsed > time_period:
                        docs_per_second = inserted_this_quantum / elapsed
                        loop_timer.reset()
                        inserted_this_quantum = 0
                        log.info(
                            f"Input:'{filename}': docs per sec:{docs_per_second:7.0f}, total docs:{total_written:>10}")
        if len(buffer) > 0:
            await collection.insert_many(buffer)
            total_written = total_written + len(buffer)

        time_finish = time.time()
        elapsed_time = time_finish - time_start

        return ImportResult(total_written, elapsed_time, filename)

    @staticmethod
    async def process_one_file(args, log, filename) -> ImportResult:

        field_file = ImportCommand.prep_field_file(args)
        q: asyncio.Queue = asyncio.Queue()
        collection, async_reader, parser = await AsyncImportCommand.async_prep_import(args, filename, field_file)
        try:
            async with TaskGroup() as tg:
                t1 = tg.create_task(AsyncImportCommand.get_csv_doc(args, q, parser, async_reader))
                t2 = tg.create_task(AsyncImportCommand.put_db_doc(args, q, log, collection, filename))

            total_documents_processed = t1.result()
            result = t2.result()
            await q.join()

            if total_documents_processed != result.total_written:
                log.error(
                    f"Total documents processed: {total_documents_processed} is not equal to  Total written: {total_written}")
                raise ValueError(
                    f"Total documents processed: {total_documents_processed} is not equal to  Total written: {total_written}")
        finally:
            if not is_url(filename):
                await async_reader.file.close()
        return result

    async def process_files(self) -> ImportResults:
        tasks = []
        results : list = []
        self.print_args(self._args)
        self._log.info("Using asyncpro")
        try:
            async with TaskGroup() as tg:
                for filename in self._args.filenames:
                    if not os.path.isfile(filename):
                        self._log.warning(f"No such file: '{i}' ignoring")
                        continue
                    task = tg.create_task(AsyncImportCommand.process_one_file(self._args, self._log, filename))
                    tasks.append(task)

            for task in tasks:
                result = task.result()
                self.report_process_one_file(self._args, result)
                results.append(result)
        except OSError as e:
            self._log.error(f"{e}")
        except exceptions.HTTPError as e:
            self._log.error(f"{e}")
        except FieldFileException as e:
            self._log.error(f"{e}")
        except _csv.Error as e:
            self._log.error(f"{e}")
        except ValueError as e:
            self._log.error(f"{e}")
        except KeyboardInterrupt:
            self._log.error(f"Keyboard interrupt... exiting")
            sys.exit(1)
        results = ImportResults(results)
        self.report_process_files(self._args, results)
        return results

    def run(self) -> ImportResults:
        return asyncio.run(self.process_files())


