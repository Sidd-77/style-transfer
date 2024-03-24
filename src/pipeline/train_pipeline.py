import os
import sys
from src.exception import CustomException
from src.logger import logging
from src.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import TrainConfig, Train



class TrainPipeline:
    def __init__(self):
        return

    def initiate_train_pipeline(self, content_file, style_file):
        try:
            ingest = DataIngestion()
            content_path, style_path = ingest.initiate_data_ingestion(content_file, style_file)
            transform = DataTransformation()
            content_image, style_image = transform.initiate_data_transformation(content_path, style_path)
            trainer = Train()
            generated_path = trainer.train(content_image, style_image)
            return generated_path
        except Exception as e :
            raise CustomException(e, sys)