import streamlit as st
from PIL import Image
import numpy as np
from model import Prediction, PredictionGPT

file = st.file_uploader("Upload an image", key="image", type=["png", "jpg", "jpeg"])

if file is not None:
    image = Image.open(file)

    st.image(
        image,
        caption=f"Uploaded Image",
        use_column_width=True,
    )

if st.session_state.image:
    answer_dict = (Prediction.get_prediction(image)[0])
    generated_stories = (PredictionGPT.get_prediction(answer_dict['generated_text'][np.random.randint(0, 4)]))
    st.text_input('Ответ:', value=answer_dict['generated_text'], disabled=True)
    st.text_input('История:', value=generated_stories['generated_text'], disable=True)
