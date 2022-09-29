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
