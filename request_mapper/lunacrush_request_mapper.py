API_END_POINT = 'https://api.lunarcrush.com/v2?'
EMPTY_STRING = '';
API_KEY = "pgmkd0a2bxqvbk5y0s34bi"
PARAM_KEY = 'key'
PARAM_DATA = 'data'
PARAM_SYMBOL = 'symbol'
PARAM_INTERVAL = 'interval'
PARAM_CHANGE = 'change'
PARAM_START = 'start'
PARAM_END = 'end'
PARAM_PAGE = 'page'
PARAM_LIMIT = 'limit'


def get_asset_data(data, symbol, interval, change, start, end):
    params = {PARAM_KEY: API_KEY}
    if data != EMPTY_STRING:
        params[PARAM_DATA] = data
    if symbol != EMPTY_STRING:
        params[PARAM_SYMBOL] = symbol
    if interval != EMPTY_STRING:
        params[PARAM_INTERVAL] = interval
    if change != EMPTY_STRING:
        params[PARAM_CHANGE] = change
    if start != EMPTY_STRING:
        params[PARAM_START] = start
    if end != EMPTY_STRING:
        params[PARAM_END] = end
    return params


def get_market_pair_data(data, symbol, limit=EMPTY_STRING, page=EMPTY_STRING):
    params = {PARAM_KEY: API_KEY}
    if data != EMPTY_STRING:
        params[PARAM_DATA] = data
    if symbol != EMPTY_STRING:
        params[PARAM_SYMBOL] = symbol
    if limit != EMPTY_STRING:
        params[PARAM_LIMIT] = limit
    if page != EMPTY_STRING:
        params[PARAM_PAGE] = page
    return params


def get_market_data(data, limit=EMPTY_STRING, sort=EMPTY_STRING):
    params = {PARAM_KEY: API_KEY}
    if data != EMPTY_STRING:
        params[PARAM_DATA] = data
    if limit != EMPTY_STRING:
        params[PARAM_LIMIT] = limit
    if sort != EMPTY_STRING:
        params[PARAM_SYMBOL] = sort
    return params
