from flask import Blueprint
from flask import request, jsonify
import requests

from db import mongo_modals
from controller import request_logger
from db.mongo_modals import Model, COLLECTION_LUNA_TIME_SERIES, CACHE_DB, MongoConnection
from request_mapper import lunacrush_request_mapper
from util import lunar_crush_util, general_util
from model import constant
from datetime import timezone, datetime, date, timedelta
from service import error_service

luna = Blueprint('luna', __name__)


@luna.route('/asset123', methods=['GET'])
def get_all_coins_test():
    start_date = datetime(2021, 8, 18)
    end_date = datetime(2021, 9, 18)
    cache_keys = lunar_crush_util.generate_key_list('BTC', start_date, end_date, constant.DAY_UNIX_TIME)
    mongo_modals.isAllIdExist(mongo_modals.getLunaTimeSeriesCollection(), cache_keys);


@luna.route('/asset', methods=['GET'])
def get_all_coins():
    start_date = datetime(2021, 8, 18)
    end_date = datetime(2021, 9, 18)
    cache_keys = lunar_crush_util.generate_key_list('BTC', start_date, end_date, constant.DAY_UNIX_TIME)
    # data = []
    # for n in range(int((end_date - start_date).days)):
    #     tmp_date = start_date + timedelta(n)
    response = request_logger.send_request(lunacrush_request_mapper.API_END_POINT,
                                           lunacrush_request_mapper.get_asset_data('assets', 'BTC', 'day', '1d',
                                                                                   general_util
                                                                                   .get_unix_timestamp_from_date(
                                                                                       start_date),
                                                                                   general_util
                                                                                   .get_unix_timestamp_from_date(
                                                                                       general_util
                                                                                           .get_next_date(
                                                                                           end_date)))
                                           )
    all_coins = response.json()
    # time_series_collection = mongo_modals.getLunaTimeSeriesCollection()
    db_connection = mongo_modals.getLunaTimeSeriesCollection()
    for n in range(len(all_coins['data'][0]['timeSeries'])):
        error_handle_json = lunar_crush_util.insert_id(all_coins['data'][0]['timeSeries'][n],
                                                       all_coins['config']['symbol'])
        if error_handle_json is None:
            return error_service.ThirdPartyError('TimeStamp Error')
        if not mongo_modals.isExists(db_connection, all_coins['data'][0]['timeSeries'][n]['_id']):
            Model.insertTimeSeriesData(
                all_coins['data'][0]['timeSeries'][n],
                db_connection)
    # flattened_json = lunar_crush_util.flatten_json(all_coins['data'][0])
    # flattened_json.pop('timeSeries')
    # data.append(flattened_json)

    # lunar_crush_util.write_to_csv(data)
    return jsonify(all_coins)


@luna.route('/marketPairs', methods=['GET'])
def get_current_market_pairs():
    response = request_logger.send_request(lunacrush_request_mapper.API_END_POINT,
                                           lunacrush_request_mapper.get_market_pair_data('market-pairs', 'BTC'))
    all_coins = response.json()
    return all_coins


@luna.route('/marketData', methods=['GET'])
def get_current_market_data():
    response = request_logger.send_request(lunacrush_request_mapper.API_END_POINT,
                                           lunacrush_request_mapper.get_market_data('market', 'acr', '10'))
    all_coins = response.json()
    return all_coins


# Top market data
@luna.route('/top/market', methods=['GET'])
def get_current_market_data_top():
    response = request_logger.send_request(lunacrush_request_mapper.API_END_POINT,
                                           lunacrush_request_mapper.get_market_pair_data('market', 'BTC', '10', '0'))
    all_coins = response.json()
    return all_coins
