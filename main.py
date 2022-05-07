from distutils.command.config import config
from api.sl_api import SLApi
from interface.cli_interface import CliInterface
from interface.inky_interface import InkyInterface
from util.config_handler import Configuration

def main():
    configuration = Configuration('./configuration.yml')
    key = configuration.load_config()['api-key']
    api = SLApi(key)
    # interface = CliInterface()
    interface = InkyInterface()
    interface.render_departures(api.get_next_departures())

if __name__ == "__main__":
    main()