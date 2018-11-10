from flask import Flask, flash, jsonify, make_response, request, render_template, redirect
import numpy as np
import base64
from PIL import Image
from models import Predictor
import cv2
import json

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

app = Flask(__name__)

#predictor = models.Predictor(None)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')
    

    
@app.route('/prediccion', methods=['GET', 'POST'])
def prediccion():
    result = "Entre"
    print(request.get_data()) #--> este es el que trae la imagen codificada en Base64.
    
    # Parseamos request y nos quedamos solo con los bytes de la imagen.
    bloque = request.get_data()[92:-47]
    
    # Resolvemos problemas de incompatibilidad.
    missing_padding = len(bloque) % 4
    if missing_padding != 0:
        bloque += b'='* (4 - missing_padding)

    # Decoficamos la imagen.
    imgdata = base64.b64decode(bloque)
    print(imgdata)
    
    # Guardamos la imagen.
    filename = 'pruebab64.jpg' 
    with open(filename, 'wb') as f:
        f.write(imgdata)
    

    # Levantamos la imagen con cv2
    path="./pruebab64.jpg"
    img = cv2.imread(path)

    # Realizamos preprocesamiento a la imagen.
    resize_img=cv2.resize(img, (28,28))
    resize_img = cv2.cvtColor(resize_img,cv2.COLOR_BGR2GRAY) 
    resize_img = resize_img / 255 
    array_img = resize_img.ravel()

    # Guardamos la imagen preprocesada.
    cv2.imwrite(path,resize_img)  

    # Envio la imagen al predictor.
    Xnew = []
    Xnew.append(array_img)

    predictor = Predictor()
    result = predictor.predecir(Xnew) 

    return jsonify(result)
    


   

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Probando errores'}), 404)

if __name__ == '__main__':
    app.run(debug = True)

