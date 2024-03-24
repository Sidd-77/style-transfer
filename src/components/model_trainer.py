import tensorflow as tf
import os
import sys
import tensorflow as tf
from src.utils import tensor_to_image
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass


@dataclass
class TrainConfig:
    gen_path:str = os.path.join('tempDir', 'generated.png')


class Train:
    def __init__(self):
        self.train_config = TrainConfig()

    def train(self, content_image, style_image):
        logging.info("Training initiated")
        try:

            model = tf.saved_model.load(os.path.join('models'))
            logging.info("Model loaded")

            generated_tensor = model(tf.constant(content_image), tf.constant(style_image))[0]
            generated_image = tensor_to_image(generated_tensor)

            generated_image.save(self.train_config.gen_path)
            logging.info("Image generated and saved")

            return self.train_config.gen_path

        except Exception as e:
            raise CustomException(e, sys)
