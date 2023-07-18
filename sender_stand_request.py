import configurations
import data
import requests


def post_new_order():
    return requests.post(configurations.URL_SERVICE + configurations.CREATE_ORDER_PATH,
           json=data.order_body)

def new_order_track_number():
    track_number = post_new_order()
    return track_number.json()['track']

def get_track_number(track):
    return requests.get(configurations.URL_SERVICE + configurations.INFO_ORDER,
           params={"t": track})
