import re
from model import Prediction
from prediction_example_data import CONTEXT

def test_model_1():
    prediction = Prediction.get_prediction('https://cdnn21.img.ria.ru/images/07e5/09/1b/1751949030_0:115:3232:1933_1920x0_80_0_0_2a7e3e8f648bd91f65451264b93ef86f.jpg')[0] 
    if 'forest' in prediction['generated_text']:
      x = True
    assert x == True
