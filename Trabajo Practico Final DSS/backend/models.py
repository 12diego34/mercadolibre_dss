import numpy as np
import pickle

CLASES = {
    0: "Auto Elevador",
    1: "Auto",
    2: "Buggy",
    3: "Camioneta",
    4: "Camion",
    5: "Colectivo",
    6: "Cuatriciclo",
    7: "Furgon",
    8: "Moto",
    9: "Pala Cargadora"
}

MODELOS = [
    {
        "nombre": 'DummyClassifier',
        "path":'modelos/CLF.pickle',
        "instancia":None
    },{
        "nombre": 'SVC',
        "path":'modelos/SVM.pickle',
        "instancia":None
    },{
        "nombre": 'KNeighborsClassifier',
        "path":'modelos/Knc.pickle',
        "instancia":None
    },{
        "nombre": 'RandomForestClassifier',
        "path":'modelos/Randomforest.pickle',
        "instancia":None
    },
    {
        "nombre": 'CNN',
        "path":'modelos/CNN.pickle',
        "instancia":None
    }
]

class AdjustVariable(object):

    """
    Used to decreases linearly the learning rate with the number of epochs,
    while we the momentum increase.
    """
    def __init__(self, name, start=0.01, stop=0.001):
        self.name = name
        self.start, self.stop = start, stop
        self.ls = None

    def __call__(self, nn, train_history):
        if self.ls is None:
            self.ls = np.linspace(self.start, self.stop, nn.max_epochs)

        epoch = train_history[-1]['epoch']
        new_value = np.float32(self.ls[epoch - 1])
        getattr(nn, self.name).set_value(new_value)



class Predictor:

    error = ""

    def __init__(self, modelo_predictor = None):
        self._modelos_cargados = self.__cargar_modelos__()      
        
    def __cargar_modelos__(self):        
        for modelo in MODELOS:
            with open(modelo.get('path'), 'rb') as f:
                try:
                    modelo['instancia'] = pickle.load(f)
                except:
                    print("Hola")
        return True

    def predecir(self, np_array):
        if not self._modelos_cargados:
            return {
                "estado": -1,
                "result":"Error: Los modelos no fueron cargados" 
            }
            
        if np_array.shape != (28,28):
            return {"estado": -2,
                    "result": "Error: Imagen debe ser 28*28 NO "+str(np_array.shape)
            }
            
        a = np_array.reshape( 1, 784)
        result = []
        for modelo in MODELOS:
            if modelo['nombre'] == 'CNN':
                a = a.reshape(-1, 1, 28,28)
            _prediccion = modelo.get('instancia').predict(a)[0]
            result.append({
                "nombre_modelo": modelo.get('nombre'),
                "label": CLASES[_prediccion]
            })

        return {
            "estado": 1,
            "result":result
        }