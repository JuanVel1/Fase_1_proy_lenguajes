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
                    print("Termino que se esta evaluando : ", termino[0])

                    if termino in self._Vt:
                        print(termino, "Es terminal !")
                        primeros.append(termino)

                    elif termino in self._Vn:
                        print(termino, "Es no terminal !")
                        primeros.append(self.primeroXTermino(termino, primeros))

                    if termino[0] in self._Vn:
                        print(termino[0], "Es no terminal !")
                        primeros = self.primeroXTermino(termino[0])
                        # si y1 no es terminal, entonces agregar prim(yl) a prim(x)
                    elif termino[0] in self._Vt:
                        print(termino[0], "Es terminal !")
                        if termino[0] not in primeros:
                            primeros.append(termino[0])
                    elif termino[0] == 'λ':
                        print(termino[0], 'Encontramos un lambda')
                        if len(termino) == 1:
                            primeros.append(termino[0])
                        else:
                            primeros.append(self.primeroXTermino(termino[1]))


            else:
                print("Termino que se esta evaluando : ", valor[0])

                if valor in self._Vt:
                    print(valor, "Es terminal !")
                    primeros.append(valor)

                elif valor in self._Vn:
                    print(valor, "Es no terminal !")
                    primeros.append(self.primeroXTermino(valor, primeros))

                if valor[0] in self._Vn:
                    print(valor[0], "Es no terminal !")
                    primeros = self.primeroXTermino(valor[0], [], {})
                    # si y1 no es terminal, entonces agregar prim(yl) a prim(x)
                elif valor[0] in self._Vt:
                    print(valor[0], "Es terminal !")
                    if valor not in primeros:
                        primeros.append(valor[0])
                elif valor[0] == 'λ':
                    print(valor[0], 'Encontramos un lambda')
                    if len(valor) == 1:
                        primeros.append(valor[0])
                    else:
                        primeros.append(self.primeroXTermino(valor[1]))
            print('Primeros de ', llave, '--> prim(', llave, ') = ', primeros)
            print("-----------------------------")

    def primeroXTermino(self, termino, primeros, total_siguientes):
        # Ingrese un termino no terminal hasta que me devuelva una lista con sus terminales
        # Recorremos las producciones para  buscar la que empieza con el termino, la coincidencia
        # {'S': 'aB|bA', 'A': 'B|aS|bAA', 'B': 'b|bS|aBB'}
        # dict_items([('E', "TE'"), ("E'", "+TE'|λ"), ('T', "FT'"), ("T'", "*FT'|λ"), ('F', 'id|(E)')])
        for no_terminal, terminos in self._P.items():
            if no_terminal == termino:
                # Recorremos sus terminos
                if terminos.count("|") > 0:
                    ter = terminos.split("|")
                    for t in ter:
                        print("Termino que se esta evaluando : ", t)
                        print("Termino que se esta evaluando : ", t[0])

                        if t in self._Vt:
                            print(t, "Es terminal !")
                            primeros.append(t)

                        elif t in self._Vn:
                            print(t, "Es no terminal !")
                            primeros.append(self.primeroXTermino(t, primeros))

                        elif t == 'λ' or t[0] == 'λ':
                            print('Encontramos un lambda')

                            simbolos_a_agregar = self.siguienteXTermino(no_terminal, total_siguientes, [])
                            for s in simbolos_a_agregar:
                                if s not in primeros:
                                    primeros.append(s)
                        if t[0] in self._Vt:
                            print(t[0], "Es terminal !")
                            primeros.append(t[0])

                        elif t[0] in self._Vn:
                            print(t[0], "Es no terminal !")
                            primeros.append(self.primeroXTermino(t[0], primeros))

                else:
                    print("Termino que se esta evaluando : ", terminos[0])

                    if terminos[0] in self._Vt:
                        print(terminos[0], "Es terminal !")
                        primeros.append(terminos[0])
                    elif terminos[0] in self._Vn:
                        print(terminos[0], "Es no terminal !")
                        self.primeroXTermino(terminos[0], primeros, {})
                    elif terminos[0] == 'λ':
                        print('Encontramos un lambda')

        return primeros

    """
    A --> αχβ
    Sig(x) -->    
    * si x es la producion inicial agregar $ a los Sig(x)
    * si ß es terminal, entonces agregar B a Sig(x)
    * si ß no es terminal entonces agregar a Sig(x) los prim(ß)
    * si ß es λ, entonces agregar a Sig(x) los sig(A)
    """

    def getSiguientes(self):
        print("Generando siguientes...")
        print(self._P.items())
        llaves = list(self._P.keys())
        valores = list(self._P.values())

        total_siguientes = {}
        # Recorremos todas las producciones
        for llave_x, valor_x in self._P.items():
            siguientes = []
            # Recorremos todos los valores de las producciones para buscar a llave
            for llave_y, valor_y in self._P.items():
                if llave_x in valor_y:
                    division = valor_y.split(llave_x)
                    caracter_posterior = division[len(division) - 1]

                    # switch del caracter que encontro
                    if caracter_posterior == " " or caracter_posterior == "":
                        print("No hay nada despues de ", llave_x, " en ", valor_y)
                        if llave_y in total_siguientes.keys():
                            for i in total_siguientes[llave_y]:
                                if i not in siguientes:
                                    siguientes.append(i)
                        else:
                            siguientes.append(self.siguienteXTermino(caracter_posterior, total_siguientes, []))
                    elif caracter_posterior in self._Vt:
                        if caracter_posterior not in siguientes:
                            siguientes.append(caracter_posterior)
                    # Si es no terminal
                    elif caracter_posterior in self._Vn:
                        simbolos_a_agregar = self.primeroXTermino(caracter_posterior, [], total_siguientes)
                        for s in simbolos_a_agregar:
                            if s not in siguientes:
                                siguientes.append(s)
                    elif '\'' in division:
                        continue
                # Valida si la llave, valor es de la primer posicion
            # if self._P.items().index((llave_x, valor_x)) == 0:

            print("llaves :", llaves)
            print("valores :", valores)
            print(llave_x)
            print(valor_x)
            if llave_x == llaves[0] and valor_x == valores[0]:
                siguientes.append('$')

            print('Siguientes de ', llave_x, '--> sig(', llave_x, ') = ', siguientes)
            total_siguientes[llave_x] = siguientes
            print('------------------------------------------------------------------')

    def siguienteXTermino(self, termino, total_siguientes, siguientes):
        for llave_y, valor_y in self._P.items():
            if termino in valor_y:
                division = valor_y.split(termino)
                caracter_posterior = division[len(division) - 1]
                if caracter_posterior == " " or caracter_posterior == "":
                    print("No hay nada despues de ", termino, " en ", valor_y)
                    ######################################################implementar
                    if llave_y in total_siguientes.keys():
                        for i in total_siguientes[llave_y]:
                            if i not in siguientes:
                                siguientes.append(i)
                    else:
                        siguientes.append(self.siguienteXTermino(caracter_posterior, total_siguientes, []))
                elif caracter_posterior in self._Vt:
                    if caracter_posterior not in siguientes:
                        siguientes.append(caracter_posterior)
                elif caracter_posterior in self._Vn:
                    simbolos_a_agregar = self.primeroXTermino(caracter_posterior, [])
                    for s in simbolos_a_agregar:
                        if s not in siguientes:
                            siguientes.append(s)
                elif '\'' in division:
                    continue
        return siguientes

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
