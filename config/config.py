import yaml


class Config():
    def __init__(self):
        stream = open('config/database.yml', 'r')
        self.database_config = yaml.load(stream, Loader=yaml.SafeLoader)


config_instance = Config()