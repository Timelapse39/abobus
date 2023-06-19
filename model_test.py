from model import Prediction


def test_model_notEmpty():
    prediction = Prediction.get_prediction(
        'https://cdnn21.img.ria.ru/images/07e5/09/1b/1751949030_0:115:3232:1933_1920x0_80_0_0_2a7e3e8f648bd91f65451264b93ef86f.jpg'
    )[0] 
    x = False
    if prediction['generated_text'] != '':
      x = True
    assert x == True

def test_model_1():
    prediction = Prediction.get_prediction(
        'https://cdnn21.img.ria.ru/images/07e5/09/1b/1751949030_0:115:3232:1933_1920x0_80_0_0_2a7e3e8f648bd91f65451264b93ef86f.jpg'
    )[0] 
    x = False
    if 'trees' or 'mountain' in prediction['generated_text']:
      x = True
    assert x == True

def test_model_2():
    prediction = Prediction.get_prediction(
        'https://media.cnn.com/api/v1/images/stellar/prod/221126143352-weston-mckennie.jpg?c=original.jpg'
    )[0] 
    x = False
    if 'soccer' or 'ball' in prediction['generated_text']:
      x = True
    assert x == True

def test_model_3():
    prediction = Prediction.get_prediction(
        'https://www.lamborghini.com/sites/it-en/files/DAM/lamborghini/facelift_2019/model_gw/aventador/gallery/aven_gate_05_m.jpg'
    )[0] 
    x = False
    if 'green' in prediction['generated_text']:
      x = True
    assert x == True

def test_model_4():
    prediction = Prediction.get_prediction(
        'https://cdnn1.ukraina.ru/img/07e6/0c/02/1041436899_0:206:2905:1840_1920x0_80_0_0_c7022893b761781d76fe592010d14bd2.jpg'
    )[0] 
    x = False
    if 'cat' in prediction['generated_text']:
      x = True
    assert x == True
