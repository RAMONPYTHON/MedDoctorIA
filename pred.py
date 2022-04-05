import numpy as np
from tensorflow.keras.preprocessing import image
from tensorflow.keras.models import load_model

modelo = load_model("modelo/modelo.h5")
status = True
    
def predict(file):
    print(" image : " + file)
    print(file)

    img = image.load_img("static/images/" + file, target_size=(150, 150))
    rgbimg = np.array(img,dtype=np.float64)
    rgbimg = rgbimg.reshape((1,150, 150,3))

    img = np.expand_dims(img, axis=0)

    print(img)
    prediction = modelo.predict(img)
    

    if np.argmax(prediction)==0: 
        print(np.argmax(prediction))   
        output="Glioma Tumor"
    if np.argmax(prediction)==1:
        print(np.argmax(prediction))
        output="Normal"
    if np.argmax(prediction)==2:
        print(np.argmax(prediction))
        output="Meningioma Tumor"
    if np.argmax(prediction)==3:
        print(np.argmax(prediction))
        output="Pituitary Tumor"
    return output