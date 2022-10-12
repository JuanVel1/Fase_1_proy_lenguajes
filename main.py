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
    #gramatica.getPrimeros()

    ## Paso 3, sacar siguientes
    print("---------------------------------------------------------------------------------")
    gramatica.getSiguientes()


"""
def crearTabla():
	import copy
	global gramatica, primeros, siguientes, terminal

	listaNT = list(gramatica.keys())
	terminales = copy.deepcopy(terminal)
	terminales.append('$')

	mat = []
	for x in gramatica:
		fila = [x]
		for y in terminales:
			fila.append('')
		mat.append(fila)

	es_gramatica_LL1 = True

	for izq in gramatica:
		der = gramatica[izq]
		for y in der:
			res = primero👍
			if 'λ' in res:
				if type(res) == str:
					primeroSiguentes = []
					fol_op = siguientes[izq]
					if fol_op is str:
						primeroSiguentes.append(fol_op)
					else:
						for u in fol_op:
							primeroSiguentes.append(u)
					res = primeroSiguentes
				else:
					res.remove('λ')
					res = list(res) +\
						list(siguientes[izq])
			ttemp = []
			if type(res) is str:
				ttemp.append(res)
				res = copy.deepcopy(ttemp)
			for c in res:
				xnt = listaNT.index(izq)
				yt = terminales.index(c)
				if mat[xnt][yt] == '':
					mat[xnt][yt] = mat[xnt][yt] \
								+ f"{izq}->{' '.join(y)}"
				else:
					if f"{izq}->{y}" in mat[xnt][yt]:
						continue
					else:
						es_gramatica_LL1 = False
						mat[xnt][yt] = mat[xnt][yt] \
									+ f",{izq}->{' '.join(y)}"

	print("\nTabla:\n")
	frmt = "{:>12}" * len(terminales)
	print(frmt.format(*terminales))

	j = 0
	for y in mat:
		frmt1 = "{:>12}" * len👍
		print(f"{listaNT[j]} {frmt1.format(*y)}")
		j += 1

	return (mat, es_gramatica_LL1, terminales)
"""
