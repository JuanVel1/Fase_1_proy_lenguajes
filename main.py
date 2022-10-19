import Control.Archivo as A
# CTRL + ALT + L --> FORMAT
from builtins import print

if __name__ == '__main__':
    print("Recuerde que los archivos con las gramaticas deben estar en la carpeta src .json")
    print("** La gramatica ya debe estar factorizada **")
    print("---------------------------------------------------------------------------------")

    archivo = A.Archivo()
    archivo.imprimirJson()
    # Creamos la instancia Gramatica
    gramatica = archivo.asignarGramatica()

    ## Paso 1, luego de leer el json validar si tiene recursiones y eliminarlas
    print("---------------------------------------------------------------------------------")
    gramatica.eliminarRecursion()
    print("Producciones: ", gramatica.getP())
    print("No terminales: ", gramatica.getVn())
    print("Terminales: ", gramatica.getVt())

    ## Paso 2, sacar primeros
    print("---------------------------------------------------------------------------------")
    gramatica.generarPrimeros()

    ## Paso 3, sacar siguientes
    print("---------------------------------------------------------------------------------")
    gramatica.generarSiguientes()

    ## Paso 4, sacar conjunto Prediccion
    print("---------------------------------------------------------------------------------")
    gramatica.conjuntoPrediccion()

    ## Paso 5, guardar tabla
    print("---------------------------------------------------------------------------------")
    gramatica.generarTabla()

    ## Paso 6, guardar tabla
    print("---------------------------------------------------------------------------------")
    gramatica.guardarTabla()
