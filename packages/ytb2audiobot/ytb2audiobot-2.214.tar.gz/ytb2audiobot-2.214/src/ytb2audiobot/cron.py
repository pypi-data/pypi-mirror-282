import asyncio
import datetime

from ytb2audiobot.datadir import get_data_dir
from ytb2audiobot.utils import delete_file_async

data_dir = get_data_dir()


async def empty_dir_by_cron(age_seconds):
    print('♻️ Empty aged items: ')
    for file in data_dir.iterdir():
        if datetime.datetime.now().timestamp() - file.stat().st_mtime > age_seconds:
            print('\t', '🔹🗑', file.name)
            await delete_file_async(file)


async def run_periodically(interval, age, func):
    while True:
        await func(age)
        await asyncio.sleep(interval)


async def run_cron():
    print('⏰  Running cron ... ')
    await run_periodically(60, 180, empty_dir_by_cron)
