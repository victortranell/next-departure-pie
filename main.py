from distutils.command.config import config
from api.sl_api import SLApi
from interface.cli_interface import CliInterface
from interface.pil_interface import PilInterface
from interface.inky_interface import InkyInterface
from util.config_handler import Configuration
from time import sleep
from datetime import datetime

def main():
    configuration = Configuration('./configuration.yml')
    key = configuration.load_config()['api-key']
    api = SLApi(key)
    # interface = CliInterface()
    #interface = PilInterface()
    interface = InkyInterface()
    shouldContinue = True
    while (shouldContinue):
        interface.render_departures(api.get_next_departures())
        sleep(calculate_sleep_time())


# This is done to not hit the rate limit of the api at 30000 req/month
def calculate_sleep_time():
    hour = datetime.now().hour

    if hour > 9:
        return 60 * 10 # every 10 mins
    elif hour < 7:
        return 60 * 30 # every 30 mins
    else:
        return 60

if __name__ == "__main__":
    main()