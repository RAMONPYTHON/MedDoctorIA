import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

saved_model = load_model("modelo/modeloTreinado.h5")
status = True

def check(input_img):
    print(" image : " + input_img)
    print(input_img)

    img = image.load_img("static/images/" + input_img, target_size=(224, 224))
    img = np.asarray(img)
    print("Imagem: " + img)

    img = np.expand_dims(img, axis=0)

    print(img)
    output = saved_model.predict(img)

    print(output)
    if output[0][0] == 1:
        status = True
    else:
        status = False

    print("Resultado do Modelo: " + status)
    return status
