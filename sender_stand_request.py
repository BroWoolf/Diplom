import configuration
import data
import requests
def create_order():
    return requests.post(configuration.URL +configuration.CREATE_PATH,
                  json = data.body).json()['track']
def get_url():
    return configuration.URL + configuration.GET_ORDER_PATH + str(create_order())

print (get_url())