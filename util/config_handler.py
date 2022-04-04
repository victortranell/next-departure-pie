import yaml

class Configuration:
    def __init__(self, path):
        self.path = path

    def load_config(self):
        with open(self.path, 'r') as file:
            configuration = yaml.load(file, Loader=yaml.FullLoader)

            print(configuration)
            return configuration