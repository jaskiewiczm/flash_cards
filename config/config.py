from yaml import load

class Config():
    def __init__():
        stream = open('config/database.yml', 'r')
        self.database_config = load(stream)


config_instance = Config()