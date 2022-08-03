# import general_data_service
import re


def filter_coin_by_id(id, input_list):
    # return filter(general_data_service.filter_method, input_list)
    # return input_list.get(id);
    result = ([x for x in input_list if x['id'] == id])
    return result


def filter_coin_by_input(input_name, input_list):
    regex = re.compile(input_name)
    matches = [x for x in input_list if re.match(regex, x['name'].lower())]
    return matches


def filter_coin_by_symbol(symbol, input_list):
    # return filter(general_data_service.filter_method, input_list)
    # return input_list.get(id);
    result = [x for x in input_list if x['symbol'] == symbol]
    return result


def filter_coin_by_param(param, param_name, input_list):
    # return filter(general_data_service.filter_method, input_list)
    # return input_list.get(id);
    result = [x for x in input_list if x[param_name] == param]
    return result


def is_contain(param, input_list):
    # return filter(general_data_service.filter_method, input_list)
    # return input_list.get(id);
    result = True if len([x for x in input_list if x == param]) > 0 else False
    return result
