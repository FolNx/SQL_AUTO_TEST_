import requests
import configuration
import data



def post_new_orders(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDERS_PATH,
        json=body,
        headers=data.headers
    )
    
def get_orders_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDERS_PATH,
        params={"t": track},
        headers=data.headers
    )

