from model.constant import PARAMETER_NONE

# https://www.coingecko.com/api/documentations/v3#/

API_HEAD = "https://api.coingecko.com/api/v3/"
PING = "/ping"
COIN_OPERATION = "coins"
MARKETS = "/markets"

LIST = "/list"
SIMPLE_OPERATION = "simple"
SUPPORTED_VS_CURRENCIES = "/supported_vs_currencies"
SEARCH_TRENDING = "search/trending"
PUBLIC_COMPANY_CRYPTO = "/companies/public_treasury/"
GLOBAL_DATA = "/global"
DEFI_DATA = "/decentralized_finance_defi"
EXCHANGE_RATES = "/exchange_rates"
EVENTS = "/events"
EVENT_COUNTRIES = "/countries"
EVENT_TYPES = "/types"

DERIVATIVES = "/derivatives"
FINANCE = '/finance'
FINANCE_PLATFORM = '_platforms'
FINANCE_PRODUCT = '_products'

EXCHANGES = "/exchanges"
STATUS_UPDATE = "/status_updates"


# -------------------------------------------PING-----------------------------------------------------------------------
# https://api.coingecko.com/api/v3/ping
def ping():
    return API_HEAD + PING


# ------------------------------------COIN_OPERATIONS-------------------------------------------------------------------

# https://api.coingecko.com/api/v3/list?include_platform=false
def get_coin_list_url(include_platform):
    return API_HEAD + COIN_OPERATION + LIST + "?include_platform=" + "false" \
        if include_platform is PARAMETER_NONE else "true"


# https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&ids=cardano%2Cbitcoin&order=market_cap_desc&per_page=100&page=1&sparkline=false&price_change_percentage=1h
def get_coin_market_details_non_crypto(ids, vs_currency, order, per_page, page, sparkline, price_change_percentage):
    return API_HEAD + COIN_OPERATION + MARKETS + "vs_currency=" + vs_currency + "&ids=" + ids \
           + "&order=" + order + "&per_page=" + per_page + "&page=" + page + "&sparkline=" \
           + sparkline + "&price_change_percentage=" + price_change_percentage


# https://api.coingecko.com/api/v3/coins/bitcoin?localization=true&tickers=true&market_data=true&community_data=true&developer_data=true&sparkline=false
def get_current_crypto_data(coin_id, localization, tickers, market_data, community_data, developer_data, sparkline):
    return API_HEAD + COIN_OPERATION + "/" + coin_id + "?localization=" + localization + "&tickers=" + tickers \
           + "&market_data=" + market_data + "&community_data=" + community_data + "&developer_data=" \
           + developer_data + "&sparkline=" + sparkline


# https://api.coingecko.com/api/v3/coins/bitcoin/tickers?exchange_ids=binance&include_exchange_logo=false&page=2&order=%20trust_score_desc&depth=false
def get_current_crypto_coin_tickers(coin_id, exchange_ids, include_exchange_logo, page, order, depth):
    return API_HEAD + COIN_OPERATION + "/" + coin_id + "tickers?exchange_ids=" + exchange_ids \
           + "&include_exchange_logo=" + include_exchange_logo + "&page=" + page + "&order=" + order + "&depth=" + depth


# https://api.coingecko.com/api/v3/coins/bitcoin/history?date=26-06-2021&localization=true
def get_coin_language_data():
    return None


# https://api.coingecko.com/api/v3/coins/cardano/market_chart?vs_currency=usd&days=1&interval=daily
def get_coin_market_chart_data(coin_id, vs_currency, days, interval):
    return API_HEAD + COIN_OPERATION + "/" + coin_id + "/market_chart?vs_currency=" \
           + vs_currency + "&days=" + days + "&interval=" + interval


# https://api.coingecko.com/api/v3/coins/cardano/market_chart/range?vs_currency=usd&from=1624544213&to=1624630613
def get_ticker_by_time(coin_id, vs_currency, unix_from, unix_to):
    return API_HEAD + COIN_OPERATION + "/" + coin_id + "/market_chart?vs_currency=" \
           + vs_currency + "&from=" + unix_from + "&to=" + unix_to


# https://api.coingecko.com/api/v3/coins/cardano/status_updates?per_page=2&page=1
def get_status_by_coin(coin_id, per_page, page):
    return API_HEAD + COIN_OPERATION + "/" + coin_id + "/status_updates" + "&per_page=" + per_page + "&page=" + page


# https://api.coingecko.com/api/v3/coins/cardano/ohlc?vs_currency=usd&days=1
def get_history_coin_data(coin_id, vs_currency, days):
    return API_HEAD + COIN_OPERATION + "/" + coin_id + "/ohlc?vs_currency=" + vs_currency + "&days=" + days


# ------------------------------------SIMPLE_OPERATIONS-----------------------------------------------------------------

# https://api.coingecko.com/api/v3/simple/supported_vs_currencies
def get_supported_vs_coin():
    return API_HEAD + SIMPLE_OPERATION + SUPPORTED_VS_CURRENCIES


# https://api.coingecko.com/api/v3/simple/price?ids=bitcoin&vs_currencies=usd&include_market_cap=true&include_24hr_vol=true&include_24hr_change=true&include_last_updated_at=true
def get_current_price_in_non_crypto(ids, vs_currencies, include_market_cap, include_24hr_vol, include_24hr_change,
                                    include_last_updated_at):
    return API_HEAD + SIMPLE_OPERATION + "/price?ids=" + ids + "&vs_currencies=" \
           + vs_currencies + "&include_market_cap=" + include_market_cap + \
           "&include_24hr_vol=" + include_24hr_vol + "&include_24hr_change=" + \
           include_24hr_change + "&include_last_updated_at=" + include_last_updated_at


# -----------------------------------TRENDING---------------------------------------------------------------------------


# https://api.coingecko.com/api/v3/search/trending
def get_trending_crypto():
    return API_HEAD + SEARCH_TRENDING


# --------------------------------------COMPANY_DETAILS-----------------------------------------------------------------


# https://api.coingecko.com/api/v3/companies/public_treasury
def get_plc_crypto_holdings(currency):
    return API_HEAD + PUBLIC_COMPANY_CRYPTO + currency


# ----------------------------------GLOBAL_DETAILS----------------------------------------------------------------------


# https://api.coingecko.com/api/v3/global
def get_crypto_global_data():
    return API_HEAD + GLOBAL_DATA


# https://api.coingecko.com/api/v3/global/decentralized_finance_defi
def get_defi_global_data():
    return API_HEAD + GLOBAL_DATA + DEFI_DATA


# -------------------------------------EXCHANGE_RATES-------------------------------------------------------------------

# https://api.coingecko.com/api/v3/exchange_rates
def get_exchange_rate_data():
    return API_HEAD + EXCHANGE_RATES


# ---------------------------------------EVENTS-------------------------------------------------------------------------


# https://api.coingecko.com/api/v3/events?country_code=US&type=Conference&page=100&upcoming_events_only=true&from_date=2020-10-28&to_date=2021-05-28
def get_events(country_code, event_type, page, upcoming_events_only, from_date, to_date):
    return API_HEAD + EVENTS + "?country_code=" + country_code + "&type=" + event_type + "&page="\
           + page + "&upcoming_events_only=" + upcoming_events_only + "&from_date=" + from_date + "&to_date=" + to_date


# https://api.coingecko.com/api/v3/events/countries
# Get list of event countries
def get_event_countries():
    return API_HEAD + EVENTS + EVENT_COUNTRIES


# https://api.coingecko.com/api/v3/events/types
# Get list of event types
def get_event_types():
    return API_HEAD + EVENTS + EVENT_TYPES


# -----------------------------------STATUS_UPDATES------------------------------------------------------------------------------------


# https://api.coingecko.com/api/v3/status_updates?category=general&project_type=Coin&per_page=20&page=2
# List all status_updates with data (description, category, created_at, user, user_title and pin)
# category
# string
# (query)
# Filtered by category (eg. general, milestone, partnership, exchange_listing, software_release, fund_movement, new_listings, event)
#
# project_type
# string
# (query)
# Filtered by Project Type (eg. coin, market). If left empty returns both status from coins and markets.
#
# per_page
# integer
# (query)
# Total results per page
# page
# integer
# (query)
# Page through results
def get_status_details_up():
    return API_HEAD + EVENTS + EVENT_TYPES


# ---------------------------------------DERIVATIVES--------------------------------------------------------------------------------

# https://api.coingecko.com/api/v3/derivatives?include_tickers=unexpired
# List all derivative tickers
def get_derivatives(include_tickers):
    return API_HEAD + DERIVATIVES + "?include_tickers=" + include_tickers


# https://api.coingecko.com/api/v3/derivatives/exchanges?order=name_desc&per_page=1&page=1
# List all derivative exchanges
def get_derivatives_exchanges(order, per_page, page):
    return API_HEAD + DERIVATIVES + "/exchanges?order=" + order + "&per_page=" + per_page + "&page=" + page


# https://api.coingecko.com/api/v3/derivatives/exchanges/bitmex?include_tickers=unexpired
# show derivative exchange data
def get_derivatives_using_exchange_data(exchange, include_tickers):
    return API_HEAD + DERIVATIVES + "/exchanges?" + exchange + "&include_tickers=" + include_tickers


# https://api.coingecko.com/api/v3/derivatives/exchanges/list
# List all derivative exchanges name and identifier
def get_valid_derivative_list(exchange, include_tickers):
    return API_HEAD + DERIVATIVES + "/exchanges/list"


# ----------------------------------------INDEXES-------------------------------------------------------------------------------

# https://api.coingecko.com/api/v3/indexes?per_page=1&page=1
# List all market indexes
def get_market_indexes(per_page, page):
    return API_HEAD + "/indexes" + "&per_page=" + per_page + "&page=" + page


# https://api.coingecko.com/api/v3/indexes/list
# List all market indexes ##################################################################################
def get_valid_indexes():
    return API_HEAD + "/indexes/list"


# -----------------------------------------FINANCE------------------------------------------------------------------------------

# https://api.coingecko.com/api/v3/finance_platforms?per_page=10
# List all finance platforms
def get_finance_platforms(per_page, page):
    return API_HEAD + FINANCE + FINANCE_PLATFORM + "&per_page=" + per_page + "&page=" + page


# https://api.coingecko.com/api/v3/finance_products?per_page=10 Contain two more params
# List all finance platforms
def get_finance_products(per_page, page):
    return API_HEAD + FINANCE + FINANCE_PRODUCT + "&per_page=" + per_page + "&page=" + page


# ----------------------------------------- EXCHANGES-------------------------------------------------------------------
# https://api.coingecko.com/api/v3/exchanges?per_page=10&page=1
def get_exchanges_with_details(per_page, page):
    return API_HEAD + EXCHANGES + "&per_page=" + per_page + "&page=" + page


# https://api.coingecko.com/api/v3/exchanges/list
def get_all_exchanges_summary():
    return API_HEAD + EXCHANGES + LIST


# https://api.coingecko.com/api/v3/exchanges/binance
def get_exchange_volume_in_btc(exchange):
    return API_HEAD + EXCHANGES + "/" + exchange


# https://api.coingecko.com/api/v3/exchanges/binance/tickers?coin_ids=cardano&include_exchange_logo=true&page=1&depth=cost_to_move_down_usd&order=trust_score_asc
def get_exchange_tickers(exchange, coin_id, include_exchange_logo, page, depth, order):
    return API_HEAD + EXCHANGES + "/" + exchange + "/tickers" + "?coin_ids=" + coin_id + "&include_exchange_logo=" \
           + include_exchange_logo + "&page=" + page + "&depth=" + depth + "&order=" + order


# https://api.coingecko.com/api/v3/exchanges/binance/status_updates?per_page=10&page=1
def get_exchange_status_update(exchange, per_page, page):
    return API_HEAD + EXCHANGES + exchange + "/" + STATUS_UPDATE + "&per_page=" + per_page + "&page=" + page


# https://api.coingecko.com/api/v3/exchanges/binance/volume_chart?days=1
def get_exchange_volume_data(exchange, days):
    return API_HEAD + EXCHANGES + exchange + "/volume_chart" + "?days" + days

# ----------------------------------------- CATEGORIES------------------------------------------------------------------

# --------------------------------------------ASSET_PLATFORM------------------------------------------------------------
