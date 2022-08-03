from util import general_util
from datetime import timezone, datetime, date, timedelta
import pandas as pd


def write_data_set(content):
    f = open("../../data-set-meta/Luna.txt", "a")
    f.write(content)
    f.close()


def dateRange(start_date, end_date):
    for n in range(int((end_date - start_date).days)):
        yield start_date + timedelta(n)


def flatten_json(json):
    json['timeSeries'].pop()
    for attribute in json['timeSeries'][0]:
        if attribute in json.keys():
            if attribute != 'time':
                json[attribute] = json['timeSeries'][0][attribute]
            else:
                json['date_time'] = datetime.utcfromtimestamp(json['timeSeries'][0][attribute])
        else:
            print(attribute + ' Has duplicates')
            json[attribute + '_time_series_'] = json['timeSeries'][0][attribute]
    return json


def write_to_csv(json):
    df = pd.DataFrame.from_dict(json)
    df.to_csv(f"../../data-set-meta/Luna_{general_util.get_unix_timestamp_from_date(datetime.now(tz=None))}.csv",
              index=None)


def insert_id(json, coin):
    if json['time'] is not None:
        json['symbol'] = str(coin).replace("\'", "")
        temp_data = generate_asset_cache_key(json['symbol'], json['time'])
        if temp_data is None:
            return None
        else:
            json['_id'] = temp_data
    return json


def generate_key_list(coin, start_date, end_date, unix_time_gap):
    return_date_arr = []
    return recursive_generate_key_add(coin, return_date_arr, general_util.get_unix_timestamp_from_date(start_date),
                                      general_util.get_unix_timestamp_from_date(end_date), unix_time_gap)


def recursive_generate_key_add(coin, arr, start_date, end_date, time_range_unix_time):
    if start_date > end_date:
        return None
    if start_date == end_date:
        arr.append(generate_asset_cache_key(coin, start_date))
        return arr
    else:
        arr.append(generate_asset_cache_key(coin, start_date))
        temp_arr = recursive_generate_key_add(coin, arr,
                                              general_util.get_next_unix_timestamp(start_date, time_range_unix_time),
                                              end_date, time_range_unix_time)
        if temp_arr is None:
            return None
        else:
            return temp_arr


def generate_asset_cache_key(coin, key_date):
    if key_date is None:
        return None
    return coin + '_' + str(key_date)
