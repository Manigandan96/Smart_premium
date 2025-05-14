import os
import gdown
from src.Smart_premium_prediction import logger
import zipfile
from src.Smart_premium_prediction.entity.config_entity import(DataIngestionconfig)

class DataIngestion:
    def __init__(self,config:DataIngestionconfig):
        self.config=config
    
    # Downloading the zip file
    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            logger.info(f"Downloading from: {self.config.source_URL}")
            gdown.download(url=self.config.source_URL, output=self.config.local_data_file, quiet=False)
            logger.info(f"Downloaded file to: {self.config.local_data_file}")
        else:
            logger.info("File already exists.")

    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)