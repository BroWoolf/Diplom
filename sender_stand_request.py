import configuration
import data
import requests
def create_order():
    return requests.post(configuration.URL +configuration.CREATE_PATH,
                  json = data.body).json()['track']
def get_order_by_track(track):
    return requests.get(configuration.URL + configuration.GET_ORDER_PATH + str(track))
