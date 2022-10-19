import json
from Entidad import Gramatica
# CTRL + ALT + L --> FORMAT
from builtins import print


class Archivo:
    def __init__(self):
        self.archivo_json = open('src/Ejemplo_3_Gramatica.json')
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
                print(self.datos['G1']['P'].items())
                for clave, valor in self.datos['G1']['P'].items():
                    clave = clave.replace('â€™', '\'')
                    valor = valor.replace('Î»', 'λ')
                    print('Produccion ', clave, ' produce --> ', valor)
                print("---------------------------------------------------------------------------------")

    def asignarGramatica(self):
        terminales = []
        noTerminales = []

        inicial = ''
        Producciones = {}
        for item in self.datos['G1']:
            if item == 'Vt':
                for terminal in self.datos['G1']['Vt']:
                    terminales.append(terminal)
            elif item == 'Vn':
                for no_terminal in self.datos['G1']['Vn']:
                    noTerminales.append(no_terminal)
            elif item == 'S':
                inicial = self.datos['G1']['S']
            elif item == 'P':
                aux = {}
                for clave, valor in self.datos['G1']['P'].items():
                    clave = clave.replace('â€™', '\'')
                    valor = valor.replace('Î»', 'λ')
                    aux[clave] = valor
                Producciones = aux
        grm = Gramatica.Gramatica(terminales, noTerminales, inicial, Producciones)
        return grm
