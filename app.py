import streamlit as st
import os
import sys
sys.path.insert(0, './')
from src.components.data_ingestion import DataIngestion, DataIngestionConfig
from src.pipeline.train_pipeline import TrainPipeline, TrainConfig
st.title(':blue[Neural :green[Style] Transfer]')

st.slider("How much proportion to apply style : ", min_value=1, max_value=5, step=1)

content_file = st.file_uploader("Choose content image", type=['jpg', 'png', 'jpeg'])
if content_file is not None:
    st.image(content_file)
    # print(type(content_file))
    # with open(os.path.join("tempDir",content_file.name),"wb+") as f:
    #      f.write(content_file.getbuffer())


style_file = st.file_uploader("Choose style image", type=['jpg', 'png', 'jpeg'])
if style_file is not None:
    st.image(style_file)
    # with open(os.path.join("tempDir",style_file.name),"wb+") as f:
    #      f.write(style_file.getbuffer())

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



