import json
from Entidad import Gramatica
# CTRL + ALT + L --> FORMAT
from builtins import print


class Archivo:
    def __init__(self):
        self.archivo_json = open('src/Ejemplo_2_Gramatica.json')
        self.datos = json.load(self.archivo_json)

    def getDatos(self):
        return self.datos

    def imprimirJson(self):
        for item in self.datos['G1']:
            if item == 'Vt':
                for terminal in self.datos['G1']['Vt']:
                    print('Terminal ', terminal)
                print("---------------------------------------------------------------------------------")
            elif item == 'Vn':
                for no_terminal in self.datos['G1']['Vn']:
                    print('No terminal ', no_terminal)
                print("---------------------------------------------------------------------------------")
            elif item == 'S':
                print('Simbolo inicial ', self.datos['G1']['S'])
                print("---------------------------------------------------------------------------------")
            elif item == 'P':
                for clave, valor in self.datos['G1']['P'].items():
                    print('Produccion ', clave, ' produce --> ', valor)
                print("---------------------------------------------------------------------------------")

    def asignarGramatica(self):
        grm = Gramatica.Gramatica()
        aux = []
        for item in self.datos['G1']:
            if item == 'Vt':
                for terminal in self.datos['G1']['Vt']:
                    aux.append(terminal)
                grm.setVt(aux)
            elif item == 'Vn':
                aux.clear()
                for no_terminal in self.datos['G1']['Vn']:
                    aux.append(no_terminal)
                grm.setVn(aux)
            elif item == 'S':
                grm.setS(self.datos['G1']['S'])
            elif item == 'P':
                aux.clear()
                grm.setP(self.datos['G1']['P'])
        return grm
