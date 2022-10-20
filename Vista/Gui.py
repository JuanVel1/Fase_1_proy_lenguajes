from Control.Archivo import Archivo

import pygame, sys, threading
from pygame.locals import *
import time
from Entidad.Gramatica import Gramatica
import json

pygame.init()
pygame.font.init()


class Gui:

    def __init__(self, gramatica):
        # pass
        self.gramatica = gramatica
        j = Archivo()
        self.x = 0  # coordenadas
        self.y = 0
        self.coun = 0
        hilo = threading.Thread(self.hilo())
        hilo.start()

    def hilo(self):
        # configuraciones iniciales pygame
        ventana = pygame.display.set_mode((900, 700))
        pygame.display.set_caption("Proyecto Estructura de Lenguajes. Fase I")
        reloj = pygame.time.Clock()
        fuente = pygame.font.SysFont('Calibri', 35, bold=True)
        posicion_base = [0, 0]

        # botones
        botonPrueba = False
        botonPrimeros = False
        botonConjunto = False

        # dibujar gramatica y gestionar eventos
        while True:
            pygame.display.update()
            ventana.fill((0, 139, 139))
            # ventana.blit(imgC, posicion_base)
            pygame.draw.rect(ventana, ((0, 0, 0)), (30, 65, 510, 130), 0)  # cuadra gramatica
            # pygame.draw.rect(ventana,(238,127,22),(200 ,5,115,43),0) #cuadra boton prueba
            pygame.draw.rect(ventana, (0, 0, 0), (30, 250, 500, 130), 0)  # cuadra boton primeros
            pygame.draw.rect(ventana, (0, 0, 0), (30, 430, 500, 130), 0)  # cuadra boton conjunto
            # pygame.draw.polygon(ventana, (0, 0, 0), ((0, 100), (0, 200), (200, 200), (200, 300), (300, 150), (200, 0), (200, 100)))
            flecha = pygame.image.load(
                r"C:\Users\once1\PycharmProjects\Proy_estructura_lenguajes\src\flecha.png")

            # pygame.draw.rect(ventana,(41, 128, 185),(10,375,115,43),0) #cuadro ffuentes
            # pygame.draw.rect(ventana,(165, 105, 189),(10,215,245,43),0) #cuadro grafo convexo

            # Encabezado gramatica
            textoGrm = fuente.render("Gramatica", True, ((0, 0, 0)))
            ventana.blit(textoGrm, (30, 35))

            # Encabezado primeros
            textoPri = fuente.render("Primeros", True, ((0, 0, 0)))
            ventana.blit(textoPri, (30, 220))
            ventana.blit(flecha, (175, 205))

            # Encabezado conjunto prediccion
            textoC = fuente.render("Conjunto prediccion", True, ((0, 0, 0)))
            ventana.blit(textoC, (30, 400))
            ventana.blit(flecha, (340, 385))

            # ventana.blit(imgX, (150, 80)) #"obstruye la arista"

            # acciones a partir de la gramatica cargada
            if self.gramatica == None:
                print("Gramatica vacia, no se puede mostrar")

            else:
                with open(r'C:\Users\once1\PycharmProjects\Proy_estructura_lenguajes\src\Ejemplo_3_Gramatica.json') as contenido:
                    info = json.load(contenido)

                    # Mostrar gramatica
                    fuenteG = pygame.font.SysFont('Calibri', 20, bold=True)

                    textoVT = []
                    textoVT.append(info['G1']['Vt'])
                    texto = fuenteG.render(str(textoVT), True, (250, 250, 250))
                    ventana.blit(texto, (80, 90))  # limite superior
                    textov = fuenteG.render("Vt: ", True, ((250, 250, 250)))
                    ventana.blit(textov, (35, 90))

                    textoVN = []
                    textoVN.append(info['G1']['Vn'])
                    texto = fuenteG.render(str(textoVN), True, (250, 250, 250))
                    ventana.blit(texto, (80, 110))  # limite superior
                    texton = fuenteG.render("Vn: ", True, ((250, 250, 250)))
                    ventana.blit(textov, (35, 110))

                    textoS = []
                    textoS.append(info['G1']['S'])
                    texto = fuenteG.render(str(textoS), True, (250, 250, 250))
                    ventana.blit(texto, (80, 130))  # limite superior
                    textos = fuenteG.render("S: ", True, ((250, 250, 250)))
                    ventana.blit(textos, (35, 130))

                    textoP = []
                    textoP.append(info['G1']['P'])
                    texto = fuenteG.render(str(textoP), True, (250, 250, 250))
                    ventana.blit(texto, (80, 150))  # limite superior
                    textocp = fuenteG.render("P: ", True, ((250, 250, 250)))
                    ventana.blit(textocp, (35, 150))

                # Funciones de los botones
                if botonPrueba:
                    # velc= 1.0
                    prueba = 'Hola'
                    # visitadosA.append(self.grafo.Amplitud("Silvestre"))
                    texto = fuenteG.render(str(prueba), True, (255, 255, 255))
                    ventana.blit(texto, (200, 15))  # limite superior

                # funcion especifica
                # self.grafo.Amplitud("Silvestre")

                # pygame.time.wait(milliseconds) #funciona pero los coloca a todos

                if botonPrimeros:
                    self.gramatica.generarPrimeros()

                    primerosP = []
                    primerosP.append(self.gramatica.getPrimeros())
                    textoPrm = fuenteG.render(str(primerosP), True, (250, 250, 250))
                    ventana.blit(textoPrm, (35, 260))  # limite superior

                if botonConjunto:
                    self.gramatica.conjuntoPrediccion()

                    conjuntoP = []
                    conjuntoP.append(self.gramatica.getConjuntoP())
                    textoCon = fuenteG.render(str(conjuntoP), True, (250, 250, 250))
                    ventana.blit(textoCon, (35, 440))  # limite superior

                # Configuraciones de botones
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == MOUSEBUTTONDOWN:
                        x_mouse, y_mouse = pygame.mouse.get_pos()

                        print(x_mouse)
                        print(y_mouse)

                        if x_mouse > 20 and x_mouse < 330 and y_mouse > 200 and y_mouse < 315:
                            botonPrimeros = True
                            print('botonPrimeros oprimido ')
                        if x_mouse > 30 and x_mouse < 405 and y_mouse > 250 and y_mouse < 420:
                            botonConjunto = True
                            print('botonconjunto oprimido ')

            reloj.tick(20)

        pygame.quit()
