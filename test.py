"""import json

archivo_json = open('src/Ejemplo_3_Gramatica.json')
datos = json.load(archivo_json)


def imprimirJson():
    for item in datos['G1']:
        if item == 'Vt':
            for terminal in datos['G1']['Vt']:
                print('Terminal ', terminal)
            print("---------------------------------------------------------------------------------")
        elif item == 'Vn':
            for no_terminal in datos['G1']['Vn']:
                print('No terminal ', no_terminal)
            print("---------------------------------------------------------------------------------")
        elif item == 'S':
            print('Simbolo inicial ', datos['G1']['S'])
            print("---------------------------------------------------------------------------------")
        elif item == 'P':
            for clave, valor in datos['G1']['P'].items():
                clave = clave.replace('â€™', '\'')
                valor = valor.replace('Î»', 'λ')
                print('Produccion ', clave, ' produce --> ', valor)
            print("---------------------------------------------------------------------------------")


cadena = "+T'|λ"
cadena = cadena.split('|')
# print(cadena)
imprimirJson()
"""

##################################################################################################

"""dic = [('E', "TE'"), ("E'", "+TE'|λ|"), ('T', "FT'"), ("T'", "*FT'|λ"), ('F', 'id|(E)')]

for termino in dic:
    if '|' in termino[1]:
        lista = termino[1].split('|')
        if '' in lista:
            lista.remove('')
        termino[1] = lista
        print(termino[1])
    else:
        print(termino[1])
"""
##################################################################################################

tabla = []
tabla = [[0 for i in range(6)] for j in range(6)]
tabla[0][0] = "VT / VN"

for columna in range(1, len(tabla[0]), 1):
    tabla[0][columna] = 1

for columna in range(1, len(tabla), 1):
    tabla[columna][0] = 2

for fila in tabla:
    print(fila)

contador = 0
for x in range(1, len(tabla)):
    for y in range(1, len(tabla[x])):
        print(tabla[x][y])
        print(contador)
        contador += 1
