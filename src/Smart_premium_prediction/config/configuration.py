from src.Smart_premium_prediction.constants import *
from src.Smart_premium_prediction.utils.common import read_yaml, create_directories
from src.Smart_premium_prediction.entity.config_entity import (DataIngestionconfig)

class ConfigurationManager:
    def __init__(self,
                 config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH,
                 schema_file_path = SCHEMA_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)
        self.schema = read_yaml(schema_file_path)

        create_directories([self.config.artifacts_root])


    def get_data_ingestion_config(self)-> DataIngestionconfig:
        config = self.config.data_ingestion
        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionconfig(
            root_dir=config.root_dir,
            source_URL = config.source_URL,
            local_data_file = config.local_data_file,
            unzip_dir = config.unzip_dir
        ) 
        
        return data_ingestion_config