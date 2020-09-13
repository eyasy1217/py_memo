import asyncio
import datetime
from dateutil import tz


def get_aware_dt():
    '''
    return datetime with timezone of os
    '''
    return datetime.datetime.now(tz=tz.gettz())


async def exec_async_sample_01(delay):
    # time-consuming process
    await asyncio.sleep(delay)

    print(delay, 'delay')


async def exec_async_sample_02():
    await asyncio.gather(
        exec_async_sample_01(1),
        exec_async_sample_01(2),
        exec_async_sample_01(3)
    )


if '__main__' == __name__:
    asyncio.run(exec_async_sample_02())


def _print_hello():
    print('hello')


def pytest_donot_call_method():
    _print_hello()
