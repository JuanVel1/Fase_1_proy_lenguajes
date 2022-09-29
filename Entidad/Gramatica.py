class Gramatica:
    def __init__(self):
        # Terminales
        self._Vt = []
        # No terminales
        self._Vn = []
        # Simbolo inicial
        self._S = ''
        # Producciones
        self._P = {}

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
