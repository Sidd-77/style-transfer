import streamlit as st
import os
import sys
sys.path.insert(0, './')

from src.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.pipeline.train_pipeline import TrainPipeline, TrainConfig
st.title(':blue[Neural :green[Style] Transfer]')
st.markdown('This project is a Neural Style Transfer application that allows users to apply the style of one image to another. ')
st.divider()


content_file = st.file_uploader("Choose content image", type=['jpg', 'png', 'jpeg'])
if content_file is not None:
    st.image(content_file, width=512)


style_file = st.file_uploader("Choose style image", type=['jpg', 'png', 'jpeg'])
if style_file is not None:
    st.image(style_file, width=512)


if st.button("Start it..."):
     obj = TrainPipeline()
     genrated_path = obj.initiate_train_pipeline(content_file, style_file)
     st.image(genrated_path)
     with open(genrated_path, "rb") as file:
        btn = st.download_button(
            label="Download image",
            data=file,
            file_name="generated.png",
            mime="image/png"
          )



