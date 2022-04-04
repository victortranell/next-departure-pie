from distutils.command.config import config
from api.sl_api import SLApi
from util.config_handler import Configuration

def main():
    configuration = Configuration('./configuration.yml')
    key = configuration.load_config()['api-key']
    api = SLApi(key)
    print(api.get_next_departure())

if __name__ == "__main__":
    main()