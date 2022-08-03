import requests
import logging
logging.basicConfig(level=logging.DEBUG)


def send_request(end_point, params):
    logging.getLogger('EXTERNAL-LOGGER').info('end-point:' + end_point + 'params:' + str(params))
    response = requests.get(end_point, params)
    logging.getLogger('EXTERNAL-LOGGER').info(response)
    return response
