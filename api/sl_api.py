from datetime import datetime
from time import sleep
import requests

ONLY_SUBWAY = 32
ONLY_BUS = 128

class SLApi:
    departure_id = 740046180 # id of station

    def __init__(self, key):
        self.key = key
        self.base_url = 'https://api.resrobot.se/v2.1/'

    def get_next_departures(self, retry = 0):
        req = requests.get(self.base_url + 'departureBoard?' + self._build_departure_query(self.departure_id, 30, ONLY_BUS) + '&accessId=' + self.key)
        if (req.status_code == 200):
            return self.handle_success(req.json())
        elif retry < 10:
            retry += 1
            sleep( self.get_exponential_backoff(retry))
            return self.get_next_departures(retry)
        return req.raise_for_status()

    def get_exponential_backoff(self, retry):
        return 10 * (2**retry)

    def _build_departure_query(self, id, duration, products):
        id = 'id=' + str(id)
        duration = 'duration=' + str(duration)
        pageSize = 'maxJourneys=10'
        passList = 'passList=0'
        language = 'language=sv'
        format = 'format=json'
        products = 'products='+str(products)

        return '&'.join([id, duration, pageSize, passList, language, format, products])

    def handle_success(self, data):
        if 'Departure' not in data:
            return []

        departures = data['Departure']

        res = []
        for departure in departures:
            timestampAsTime = datetime.strptime(departure['time'], "%H:%M:%S").time()
            res.append({'time': timestampAsTime.strftime("%H:%M"), 'direction': departure['direction']})

        return res 

