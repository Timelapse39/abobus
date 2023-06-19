from functools import cache
import streamlit as st
from transformers AutoTokenizer, pipeline, set_seed
from PIL import Image

MODEL = "nlpconnect/vit-gpt2-image-captioning"
MODELGPT = "gpt2"


class Prediction:
    @staticmethod
    @cache
    @st.cache(allow_output_mutation=True)
    def get_model():
        tokenizer = AutoTokenizer.from_pretrained(MODEL)
        nlp = pipeline("image-to-text", model="nlpconnect/vit-gpt2-image-captioning",
                       tokenizer=tokenizer)
        return nlp

    @staticmethod
    def get_prediction(image: Image):
        if not image: return
        image_to_text = Prediction.get_model()
        temp_var = image_to_text(image)
        return temp_var


class PredictionGPT:
    @staticmethod
    def get_prediction(text: str):
        generator = pipeline('text-generation', model=MODELGPT)
        set_seed(1337)
        generator("Here is a story about: " + text, max_length=300,
                  num_return_sequences=5)
        return generator;
