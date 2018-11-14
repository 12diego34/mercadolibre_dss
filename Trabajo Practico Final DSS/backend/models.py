import numpy as np
from sklearn.externals import joblib

CLASES = {
    0: "Auto",
    1: "Buggy",
    2: "Camion",
    3: "Camioneta",
    4: "Colectivo",
    5: "Cuatriciclo",
    6: "Furgon",
    7: "Moto",
    8: "Pala Cargadora"
}

MODELOS = [
    {
        "nombre": 'DummyClassifier',
        "path":'modelos/dummy.joblib',
        "instancia":None
    },{
        "nombre": 'SVM (poly grado 2)',
        "path":'modelos/svm2.joblib',
        "instancia":None
    },{
        "nombre": 'SVM (poly grado 3)',
        "path":'modelos/svm3.joblib',
        "instancia":None
    },{
        "nombre": 'KNeighborsClassifier',
        "path":'modelos/kneigh.joblib',
        "instancia":None
    },{
        "nombre": 'RandomForestClassifier',
        "path":'modelos/randomforest.joblib',
        "instancia":None
    }
    #{
     #   "nombre": 'CNN',
      #  "path":'modelos/CNN.joblib',
       # "instancia":None
    #}
]

class Predictor:

    error = ""

    def __init__(self, modelo_predictor = None):
        self._modelos_cargados = self.__cargar_modelos__()      
        
    def __cargar_modelos__(self):        
        for modelo in MODELOS:
            with open(modelo.get('path'), 'rb') as f:
                try:
                    modelo['instancia'] = joblib.load(f) 
                except:
                    print("Hola")
        return True

    def predecir(self, imagen):
        if not self._modelos_cargados:
            return {
                "estado": -1,
                "result":"Error: Los modelos no fueron cargados" 
            }
            
        #if np_array.shape != (28,28):
         #   return {"estado": -2,
          #          "result": "Error: Imagen debe ser 28*28 NO "+str(np_array.shape)
           # }
            
        #a = np_array.reshape( 1, 784)
        result = []
        for modelo in MODELOS:
            #if modelo['nombre'] == 'CNN':
             #   a = a.reshape(-1, 1, 28,28)
            _prediccion = modelo.get('instancia').predict(imagen)
            result.append({
                "nombre_modelo": modelo.get('nombre'),
                "label": CLASES[_prediccion[0]]
            })

        return {
            "estado": 1,
            "result":result
        }