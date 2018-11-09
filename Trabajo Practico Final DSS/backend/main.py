from flask import Flask, flash, jsonify, make_response, request, render_template, redirect
import numpy as np
import base64
from PIL import Image
#import models
from models import AdjustVariable
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
    result = "HOLA"
    print(request.get_data()) #--> este es el que trae la imagen.
    print("==========")
    print(request.get_json())
    #return jsonify(result)
    print(len(request.get_data()))
    print("======")
    print(request)


    #bloque = request.get_data().decode('utf8').replace("'", '"')
    bloque = request.get_data()[92:-47]
    #data = json.loads(my_json)
    

    #sub_string_remove = "b'------WebKitFormBoundaryvhOnfw5y4gYgefjs\r\nContent-Disposition: form-data; name="
    #bloque.replace("b'------","")#kc0qfcvaQMflBquV
    #bloque.replace("WebKitFormBoundary","")
    #bloque[100:-52]
    #print(bloque[92:-47])
    #bloque = bloque[92:-47]
    print(bloque)
    print(type(bloque))
    
    
    missing_padding = len(bloque) % 4
    if missing_padding != 0:
        bloque += b'='* (4 - missing_padding)



    #=\r\n------WebKitFormBoundarykc0qfcvaQMflBquV--\r\n'
    imgdata = base64.b64decode(bloque)
    print(imgdata)
    
    #fh = open("pruebab64.jpg", "wb")
    #fh.write(bloque.decode('base64'))
    #fh.close()
    
    
    filename = 'pruebab64.jpg' 
    with open(filename, 'wb') as f:
        f.write(imgdata)
    

    return jsonify(result)
    

    """
    if request.method == 'POST' and 'inputImagen' in request.imagen:
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
    """

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Probando errores'}), 404)

if __name__ == '__main__':
    app.run(debug = True)

def decode_base64(data):
    """Decode base64, padding being optional.

    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    missing_padding = len(data) % 4
    if missing_padding != 0:
        data += b'='* (4 - missing_padding)
    return base64.decodestring(data)