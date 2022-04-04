import requests

class SLApi:
    def __init__(self, key):
        self.key = key
        self.base_url = 'https://api.resrobot.se/v2.1/'

    def get_next_departure(self):
        return requests.get(self.base_url+'departureBoard?id=740021670&duration=15&maxJourneys=10&passList=0&lang=sv&format=json'+'&accessId='+self.key)