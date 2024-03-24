import os
import sys
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass
import shutil


@dataclass
class DataIngestionConfig : 
    dir_path:str = os.path.join('tempDir')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()
        return

    def initiate_data_ingestion(self, content_file, style_file):
        logging.info("Entered data ingestion")
        try:
            if os.path.exists(self.ingestion_config.dir_path):
                shutil.rmtree(self.ingestion_config.dir_path)
            os.makedirs(self.ingestion_config.dir_path)

            content_path = os.path.join(self.ingestion_config.dir_path,'content'+ os.path.splitext(content_file.name)[1])
            style_path = os.path.join(self.ingestion_config.dir_path, 'style' + os.path.splitext(style_file.name)[1])

            with open(content_path, "wb+") as f:
                f.write(content_file.getbuffer())
            with open(style_path, "wb+") as f:
                f.write(style_file.getbuffer())

            logging.info("files saved")

            return (
                content_path,
                style_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__=="__main__":
    obj = DataIngestion()
    obj.initiate_data_ingestion()