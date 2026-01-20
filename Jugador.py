from Ficha import Ficha
from Tablero import Tablero

import random

class Jugador:
    def __init__(self, nombre, ficha, es_ia=False, nivel_ia=1, num_fichas=4):
        self.nombre = nombre
        self.ficha = ficha
        self.es_ia = es_ia
        self.nivel_ia = nivel_ia
        self.num_fichas = num_fichas

    def elegir_columna(self, tablero):
        if self.es_ia:
            if self.nivel_ia == 1:
                return self.iaNivel1(tablero)
            else:
                return self.iaNivel2(tablero)
        else:
            return self._humano(tablero)

    def _humano(self, tablero):
        while True:
            try:
                col = int(input(f"{self.nombre}, elige columna: ")) - 1
                if 0 <= col < tablero.ancho and not tablero.columna_llena(col):
                    return col
                print("Columna inválida o llena")
            except ValueError:
                print("Introduce un número válido")

    def iaNivel1(self, tablero):
        columnas = [c for c in range(tablero.ancho) if not tablero.columna_llena(c)]
        return random.choice(columnas)

    def iaNivel2(self, tablero):
        columnas = [c for c in range(tablero.ancho) if not tablero.columna_llena(c)]
        ficha_rival = Ficha.CIRCULO if self.ficha == Ficha.EQUIS else Ficha.EQUIS

        for c in columnas:
            if tablero.simular_gana(c, self.ficha, self.num_fichas):
                return c

        for c in columnas:
            if tablero.simular_gana(c, ficha_rival, self.num_fichas):
                return c

        mejor = -1
        mejores = []
        for c in columnas:
            valor = tablero.fichas_en_linea(c, self.ficha)
            if valor > mejor:
                mejor = valor
                mejores = [c]
            elif valor == mejor:
                mejores.append(c)

        return random.choice(mejores)
