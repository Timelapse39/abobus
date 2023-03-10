from functools import cache
import streamlit as st
from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline
from PIL import Image

MODEL = "nlpconnect/vit-gpt2-image-captioning"


class Prediction:
    @staticmethod
    @cache
    @st.cache(allow_output_mutation=True)
    def get_model():
        tokenizer = AutoTokenizer.from_pretrained(MODEL)
        nlp = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning", tokenizer=tokenizer)
        return nlp

    @staticmethod
    def get_prediction(image: Image):
        if not image: return
        image_to_text = Prediction.get_model()
        temp_var = image_to_text(image)
        return temp_var