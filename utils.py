import datetime
from dateutil import tz


def get_aware_dt():
    '''
    return datetime with timezone of os
    '''
    return datetime.datetime.now(tz=tz.gettz())

