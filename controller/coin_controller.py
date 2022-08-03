from flask import Blueprint
from flask import request, jsonify
import requests
from werkzeug.exceptions import BadRequest

from request_mapper import gecko_request_mapper
from model import server_models
from model import constant

from service import coin_data_service
from service import error_service
from service import general_data_service
from service.error_service import WrongParam

coin = Blueprint('coin', __name__)


@coin.route("/ping")
def index():
    server_models.create_status(constant.ping_success)
    return server_models.create_status(constant.ping_success)


# ---------------------------------------------------------COIN_REQUESTS---------------------------------------------------------------------------------------
@coin.route('all/coins', methods=['GET'])
def get_all_coins():
    response = requests.get(gecko_request_mapper.get_coin_list_url(constant.PARAMETER_NONE))
    all_coins = response.json()
    return jsonify(all_coins)


@coin.route('all/coins/name', methods=['GET'])
def get_all_coins_name():
    response = requests.get(gecko_request_mapper.get_coin_list_url(constant.PARAMETER_NONE))
    all_coins = response.json()
    return jsonify(all_coins)


@coin.route('filter/coin/id', methods=['GET'])
def get_filter_coin_by_id():
    # flag to include platform contract addresses (eg. 0x… for Ethereum based tokens).
    # query_parameters = request.args

    # platform = query_parameters.get('platform')
    filter_coin = request.args.get('filterCoin')
    # filter_choice = request.args.get('choice')
    if filter_coin is None:
        return BadRequest()

    third_party_response = requests.get(gecko_request_mapper.get_coin_list_url(constant.PARAMETER_NONE))
    all_coins = third_party_response.json()
    # filter_param = constant.filter_by_id \
    #     if filter_choice == constant.filter_by_id else None
    # filter_param = constant.filter_by_symbol \
    #     if filter_param != constant.filter_by_symbol & filter_choice == constant.filter_by_symbol else None
    # if filter_param is None:
    #     return WrongParam("choice Unrecognized")
    response = coin_data_service.filter_coin_by_id(filter_coin.lower(), all_coins)
    return jsonify(response)


@coin.route('filter/coin/input', methods=['GET'])
def get_filter_coin_by_input():
    filter_coin = request.args.get('filterCoin')
    if filter_coin is None:
        return BadRequest()
    third_party_response = requests.get(gecko_request_mapper.get_coin_list_url(constant.PARAMETER_NONE))
    all_coins = third_party_response.json()
    response = coin_data_service.filter_coin_by_input(filter_coin.lower(), all_coins)
    return jsonify(response)


@coin.route('filter/coin/symbol', methods=['GET'])
def get_filter_coin_by_symbol():
    filter_coin = request.args.get('filterCoin')
    if filter_coin is None:
        return BadRequest()
    third_party_response = requests.get(gecko_request_mapper.get_coin_list_url(constant.PARAMETER_NONE))
    all_coins = third_party_response.json()
    response = coin_data_service.filter_coin_by_symbol(filter_coin.lower(), all_coins)
    return jsonify(response)


@coin.route('filter/coin/priceData', methods=['GET'])
def get_history_chart_ohlc_data():
    coin_id = request.args.get('coinId')
    vs_currency = request.args.get('vsCurrency')
    days = request.args.get('days')
    if coin_id is None or vs_currency is None or days is None:
        return BadRequest()
    third_party_response = requests.get(gecko_request_mapper.get_history_coin_data(coin_id, vs_currency, days))
    all_coins = third_party_response.json()
    return jsonify(all_coins)


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------

# ---------------------------------------------------------SIMPLE_REQUESTS---------------------------------------------------------------------------------------


@coin.route('/simple/vsCoin', methods=['GET'])
def get_all_vs_coin():
    third_party_response = requests.get(gecko_request_mapper.get_supported_vs_coin())
    all_coins = third_party_response.json()
    return jsonify(all_coins)


@coin.route('/simple/select/vsCoin', methods=['GET'])
def select_vs_non_crypto_coin():
    selected_coin = request.args.get('selected')
    if selected_coin is None:
        return BadRequest()
    third_party_response = requests.get(gecko_request_mapper.get_supported_vs_coin())
    all_vs_coins = third_party_response.json()
    return server_models.create_status(constant.ACTION_SUCCESS
                                       if coin_data_service.is_contain(selected_coin,
                                                                       all_vs_coins) else constant.ACTION_FAIL)


@coin.route('/market/details', methods=['GET'])
def get_coin_market_detail_non_crypto_coin():
    crypto_ids = request.args.get('ids')
    vs_coins = request.args.get('vsCoin')
    include_market_cap = "false" if request.args.get('include_market_cap') is None else "true"
    include_24hr_vol = "false" if request.args.get('include_24hr_vol') is None else "true"
    include_24hr_change = "false" if request.args.get('include_24hr_change') is None else "true"
    include_last_updated_at = "false" if request.args.get('include_last_updated_at') is None else "true"
    if crypto_ids is None or vs_coins is None:
        return server_models.server_error_status(constant.ACTION_FAIL, error_service.THIRD_PARTY_ERROR)
    third_party_response = requests.get(
        gecko_request_mapper.get_current_price_in_non_crypto(crypto_ids, vs_coins, include_market_cap, include_24hr_vol,
                                                             include_24hr_change, include_last_updated_at))
    if third_party_response.status_code != 200:
        return server_models.server_error_status(constant.ACTION_FAIL, error_service.THIRD_PARTY_ERROR)
    return jsonify(third_party_response.json())


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------


# ------------------------------------------------------------------------TRENDING-----------------------------------------------------------------------------


@coin.route('/search/trending', methods=['GET'])
# Top-7 trending coins on CoinGecko as searched by users in the last 24 hours (Ordered by most popular first)
def get_trending_coins():
    third_party_response = requests.get(
        gecko_request_mapper.get_trending_crypto())
    if third_party_response.status_code != 200:
        return server_models.server_error_status(constant.ACTION_FAIL, error_service.THIRD_PARTY_ERROR)
    return jsonify(third_party_response.json())


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------CRYPTO_GLOBAL-----------------------------------------------------------------------------


@coin.route('/search/global/crypto', methods=['GET'])
# Get cryptocurrency global data
def get_crypto_global_data():
    third_party_response = requests.get(
        gecko_request_mapper.get_crypto_global_data())
    if third_party_response.status_code != 200:
        return server_models.server_error_status(constant.ACTION_FAIL, error_service.THIRD_PARTY_ERROR)
    return jsonify(third_party_response.json())


@coin.route('/search/global/defi', methods=['GET'])
# Get Top 100 Cryptocurrency Global Decentralized Finance(defi) data
# defi_market_cap
# Defi Market Capitalization in USD
# eth_market_cap
# Ethereum Market Capitalization in USD
# defi_to_eth_ratio
# defi_market_cap to eth_market_cap ratio
#
# trading_volume_24h
# defi trading volume in 24h in USD
# defi_dominance
# defi_market_cap to total_market_cap ratio
#
# top_coin_name
# defi coin with largest market_cap
#
# top_coin_dominance
# top defi coin market dominance
def get_defi_global_data():
    third_party_response = requests.get(
        gecko_request_mapper.get_defi_global_data())
    if third_party_response.status_code != 200:
        return server_models.server_error_status(constant.ACTION_FAIL, error_service.THIRD_PARTY_ERROR)
    return jsonify(third_party_response.json())


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------COMPANIES-----------------------------------------------------------------------------


@coin.route('/search/holdings', methods=['GET'])
# Get public companies bitcoin or ethereum holdings (Ordered by total holdings descending)
def get_company_holdings():
    currency = request.args.get('currency')
    if currency != "bitcoin" and currency != "ethereum":
        return server_models.server_error_status_with_expected(constant.ACTION_FAIL, error_service.INVALID_INPUT,
                                                               "bitcoin or ethereum")
    third_party_response = requests.get(
        gecko_request_mapper.get_plc_crypto_holdings(currency))
    if third_party_response.status_code != 200:
        return server_models.server_error_status(constant.ACTION_FAIL, error_service.THIRD_PARTY_ERROR)
    return jsonify(third_party_response.json())


# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# ------------------------------------------------------------------------EXCHANGE_RATES-----------------------------------------------------------------------------


@coin.route('/search/exchangeRates', methods=['GET'])
# Get BTC-to-Currency exchange rates
def get_exchange_rates():
    third_party_response = requests.get(
        gecko_request_mapper.get_exchange_rate_data())
    if third_party_response.status_code != 200:
        return server_models.server_error_status(constant.ACTION_FAIL, error_service.THIRD_PARTY_ERROR)
    return jsonify(third_party_response.json())
# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
