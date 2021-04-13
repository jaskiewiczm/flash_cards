from config.config import config_instance


class Database():
    def init(self):
        self.engine = create_engine(self.connection_string())
        self.base = declarative_base()

    def connection_string(self):
        user = config_instance.database_config['user']
        password = config_instance.database_config['password']
        database = config_instance.database_config['database']
        host = config_instance.database_config['host']
        port = config_instance.database_config['port']

        conn_string = f'mysql:///?User={user}&;Password={password}&Database={database}&Server={host}&Port={port}'
        print(conn_string)
        return conn_string

database_instance = Database()