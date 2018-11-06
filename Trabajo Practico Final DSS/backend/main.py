from flask import Flask, flash, jsonify, make_response, request, render_template, redirect
import numpy as np
import base64
from PIL import Image
#import models
from models import AdjustVariable
import cv2

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
    result = "HOLA"
    #return jsonify(result)
    
    if request.method == 'POST' and 'inputImagen' in request.files:
        foto = request.files['inputImagen']
        result = "CHAU"
        if foto == None or not allowed_file(foto.filename):
            result = "Archivo incorrecto"
        else:
            #s = "tmp.png"
            #foto.save(s)
            print("=================")
            result = type(foto) 
            cv2.imwrite("C:/Users/Asus/Documents/mercadolibre_dss/Trabajo Practico Final DSS/backend",foto) 
            #i = cv2.imread('tmp.png', 0)
            #i = np.asarray(Image.open(s))
           # result = predictor.predecir(i) 
    else:
        result = "CAPO"         

    return jsonify(result)
    

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Probando errores'}), 404)

if __name__ == '__main__':
    app.run(debug = True)