import datetime
from dateutil import tz


def get_aware_dt():
    '''
    return datetime with timezone of os
    '''
    return datetime.datetime.now(tz=tz.gettz())

def _print_hello():
    print('hello')

def pytest_donot_call_method():
    _print_hello()
