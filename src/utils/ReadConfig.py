import configparser
import os


class ConfigReader:
    def __init__(self):
        self.cf = configparser.ConfigParser()
        current_path = os.path.dirname(__file__)
        env = os.getenv('ENV')
        config_file_name = '{env}.ini'.format(env=env) if env else 'config.ini'
        self.cf.read('{cur_dir}/../config/{file_name}'.format(cur_dir=current_path, file_name=config_file_name))

    def get_ds_config(self, ds_name: str) -> dict:
        options = self.cf.items(ds_name)
        return dict((key, value) for key, value in options)
