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

    def eliminarRecursion(self):
        # A+ BIA' | BA'|... | BA'
        # A' → QA’ | Q2A' | ... | AmAla

        terminos_independientes = []
        terminos_asociativos = []
        llave_prima = ''

        for llave, valor in self._P.items():
            hay_recursion = False
            if valor.count("|") > 0:  # Si contiene el separador  |
                valores = valor.split("|")  # Se obtiene cada conjunto
                terminos_asociativos.clear()
                terminos_independientes.clear()
                for val in valores:
                    if val.startswith(llave):
                        print("Se encontro recursion : ", llave, " --> ", val)
                        terminos_asociativos.append(val.removeprefix(llave))
                        hay_recursion = True
                    else:
                        terminos_independientes.append(val)

            print("Terminos asociativos: ")
            for ta in terminos_asociativos:
                if hay_recursion:
                    ta += llave + '\''
                print(ta)

            print("Terminos independientes: ")
            for ti in terminos_independientes:
                if hay_recursion:
                    ti += llave + '\''
                print(ti)

            else:
                if valor.startswith(llave):
                    print("Se encontro recursion : ", llave, " --> ", valor)
                    llave_prima = llave + '\''

            if hay_recursion:
                self.actualizarProduccion(llave, terminos_independientes)

            print("--------------------------------------")
        """
        self.actualizarProduccion(llave, aux1)
        self.actualizarProduccion(llave + '\'', aux2)
        """
