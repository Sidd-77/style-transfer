import sys
import os
import numpy as np
from src.exception import CustomException
from src.logger import logging
from src.utils import load_img


class DataTransformation:
    def __init__(self) -> None:
        return

    def initiate_data_transformation(self, content_path, style_path):
        logging.info("Data transformation initated")

        try:
            content_image = load_img(content_path)
            style_image = load_img(style_path)
            logging.info("Images processed")

            return (
                content_image,
                style_image
            )

        except Exception as e:
            raise CustomException(e, sys)
