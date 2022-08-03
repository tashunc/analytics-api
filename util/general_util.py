from datetime import timezone, datetime, date, timedelta
from model import constant


def add_to_array(data, array):
    if data is None:
        return None
    else:
        array.append(data)


def get_next_unix_timestamp(start_date, time_range):
    if start_date is None:
        return None
    else:
        return start_date + time_range


def get_next_date(previous_date):
    return previous_date + timedelta(days=1)


def get_unix_time_tomorrow(start_date):
    if start_date is None:
        return None
    else:
        return start_date + constant.DAY_UNIX_TIME


def get_unix_timestamp(year, month, day, hours=0, minutes=0, seconds=0, milliseconds=0):
    dt = datetime(year, month, day, hours, minutes, seconds, milliseconds)
    return dt.replace(tzinfo=timezone.utc).timestamp()


def get_unix_timestamp_from_date(input_date):
    return int(input_date.replace(tzinfo=timezone.utc).timestamp())
