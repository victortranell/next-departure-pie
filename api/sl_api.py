from datetime import datetime
import requests

ONLY_SUBWAY = 32

class SLApi:
    departure_id = 740021670 # id of station

    def __init__(self, key):
        self.key = key
        self.base_url = 'https://api.resrobot.se/v2.1/'

    def get_next_departures(self, retry = 0):
        req = requests.get(self.base_url + 'departureBoard?' + self._build_departure_query(self.departure_id, 30, ONLY_SUBWAY) + '&accessId=' + self.key)

        if (req.status_code == 200):
            return self.handle_success(req.json())
        elif retry < 2:
            retry += 1
            return self.get_next_departures(retry)
        return req.raise_for_status()

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

