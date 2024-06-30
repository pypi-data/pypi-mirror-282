import asyncio
import datetime
import pathlib

from ytb2audiobot.datadir import get_data_dir
from ytb2audiobot.utils import delete_file_async

from ytb2audiobot.utils import async_iterdir

data_dir = get_data_dir()


async def empty_dir_by_cron(age_seconds):
    for file in data_dir.iterdir():
        if int(datetime.datetime.now().timestamp()) - int(file.stat().st_ctime) > age_seconds:
            await delete_file_async(file)


async def run_periodically(interval, age, func):
    while True:
        await func(age)
        await asyncio.sleep(interval)


async def run_cron():
    print('⏰  Running cron ... ')
    await run_periodically(60, 3600, empty_dir_by_cron)
