import os
import urllib.request as request
import zipfile
from textSummarize.logging import logger
from textSummarize.utils.common import get_size
from textSummarize.entity import DataIngestionConfig
from pathlib import Path

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_file(self):
        if not os.path.exists(self.config.local_data_file):
            file_name, header = request.urlretrieve(
                url=self.config.source_URL,
                filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file: {file_name} with headers: {header}")
        else:
            logger.info(f"File already exists. Size: {get_size(Path(self.config.local_data_file))} KB")

    def extract_zip_file(self):
        unzip_path = self.config.unzip_dir
        os.makedirs(unzip_path, exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)
            logger.info(f"Extracted files to: {unzip_path}")