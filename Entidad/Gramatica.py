class Gramatica:
    def __init__(self, Vt, Vn, S, P):
        # Terminales
        self._Vt = Vt
        # No terminales
        self._Vn = Vn
        # Simbolo inicial
        self._S = S
        # Producciones
        self._P = P

    def setVt(self, vt):
        self._Vt = vt

    def setVn(self, vn):
        self._Vn = vn

    def setS(self, s):
        self._S = s

    def setP(self, p):
        self._P = p

    def getVt(self):
        return self._Vt

    def getVn(self):
        return self._Vn

    def getS(self):
        return self._S

    def getP(self):
        return self._P

    def actualizarProduccion(self, llave, valor):
        self._P[llave] = valor

    def actualizarProduccion_nueva(self, llave, valor):
        self._P[llave] = valor + '|λ'

    def eliminarRecursion(self):
        # A+ BIA' | BA'|... | BA'
        # A' → QA’ | Q2A' | ... | AmAla

        terminos_independientes = []
        terminos_asociativos = []
        llave_prima = ''
        producciones_nuevas = []
        termino_aparte = ''

        for llave, valor in self._P.items():
            terminos_asociativos.clear()
            terminos_independientes.clear()
            hay_recursion = False

            if valor.count("|") > 0:  # Si contiene el separador  |
                valores = valor.split("|")  # Se obtiene cada conjunto
                for val in valores:
                    if val.startswith(llave):
                        print("Se encontro recursion : ", llave, " --> ", val)
                        terminos_asociativos.append(val.removeprefix(llave) + llave + '\'')
                        hay_recursion = True
                    else:
                        terminos_independientes.append(val + llave + '\'')

                if hay_recursion:
                    if len(terminos_independientes) > 0:
                        terminos = ''
                        for termino in terminos_independientes:
                            terminos += termino + '|'
                        terminos = terminos.removesuffix('|')
                        self.actualizarProduccion(llave, terminos)
                    if len(terminos_asociativos) > 0:
                        terminos = ''
                        for termino in terminos_asociativos:
                            terminos += termino + '|'
                        terminos = terminos.removesuffix('|')
                        producciones_nuevas.append((
                            llave + '\'', terminos
                        ))

            else:
                if valor.startswith(llave):
                    print("Se encontro recursion : ", llave, " --> ", valor)
                    llave_prima = llave + '\''
                    hay_recursion = True
                    termino_aparte = valor.removeprefix(llave)
                if hay_recursion:
                    self.actualizarProduccion(llave, llave_prima)
                    producciones_nuevas.append((
                        llave + '\'', termino_aparte + llave + '\''
                    ))

        if len(producciones_nuevas) > 0:
            for pn in producciones_nuevas:
                self.actualizarProduccion_nueva(pn[0], pn[1])
            print("****")
        print("--------------------------------------")

    """
    Formula general
    X→ y1,y2,y3.....yk
    y1...→ VT 6 VN
    prim(x) → si y1 es terminal, entonces agregar y1 a prim(x)
              si y1 no es terminal, entonces agregar prim(yl) a prim(x)
              si y1 es , entonces agregar prim(y2) a prim(x)
              si y1 hasta yk tiene 1, entonces agregar a prim(x)
    """

    def getPrimeros(self):
        print("Generando primeros...")

        # Recorremos cada produccion
        print(self._P.items())
        for llave, valor in self._P.items():
            primeros = []
            # Recorremos cada termino
            if valor.count("|") > 0:
                valores = valor.split("|")
                # Se obtiene cada conjunto
                print("Valores : ", valores)
                print("No terminales : ", self._Vt)
                for termino in valores:
                    if termino[0] in self._Vn:
                        print(termino[0], "Es no terminal !")
                        primeros = self.primeroXTermino(termino[0])
                        # si y1 no es terminal, entonces agregar prim(yl) a prim(x)
                    elif termino[0] in self._Vt:
                        print(termino[0], "Es terminal !")
                        if termino[0] not in primeros:
                            primeros.append(termino[0])

            else:
                if valor in self._Vn:
                    print(valor, "Es no terminal !")
                    primeros = self.primeroXTermino(valor)
                    # si y1 no es terminal, entonces agregar prim(yl) a prim(x)
                elif valor in self._Vt:
                    print(valor, "Es terminal !")
                    if valor not in primeros:
                        primeros.append(valor)

            print('Primeros de ', llave, '--> prim(', llave, ') = ', primeros)

    def primeroXTermino(self, termino):
        # Ingrese un termino no terminal hasta que me devuelva un terminal
        # Recorremos las producciones para  buscar la que empieza con el termino, la coincidencia
        # {'S': 'aB|bA', 'A': 'B|aS|bAA', 'B': 'b|bS|aBB'}
        primeros = []
        for no_terminal, terminos in self._P.items():
            if no_terminal == termino:
                for termino in terminos:
                    if termino[0] in self._Vt:
                        primeros.append(termino[0])
                    else:
                        primeros = self.primeroXTermino(termino[0])
                        return primeros
        return primeros

    """


	if len(regla) != 0:
		if regla[0] in list(gramatica.keys()):
			lista = []
			der_reglas = gramatica[regla[0]]
			for itr in der_reglas:
				indivRes = primero(itr)
				if type(indivRes) is list:
					for i in indivRes:
						lista.append(i)
				else:
					lista.append(indivRes)

			if '#' not in lista:
				return lista
			else:
				nuevaLista = []
				lista.remove('#')
				if len(regla) > 1:
					nuevaRes = primero(regla[1:])
					if nuevaRes != None:
						if type(nuevaRes) is list:
							nuevaLista = lista + nuevaRes
						else:
							nuevaLista = lista + [nuevaRes]
					else:
						nuevaLista = lista
					return nuevaLista
				lista.append('#')
				return lista
    """

    def getSiguientes(self):
        # Crear codigo para generar los siguientes de cada produccion
        """
        # Producciones
        self._P = {} --> Conjunto de producciones con llave no terminal y valores correspondientes a sus producciones
        separadas por  |
        """
        pass
