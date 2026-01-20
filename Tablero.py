from Ficha import Ficha

class Tablero:
    def __init__(self, alto, ancho):
        self.alto = alto
        self.ancho = ancho
        self.celdas = [[Ficha.VACIA for _ in range(ancho)] for _ in range(alto)]

    def mostrar(self, fila_ultima=None, col_ultima=None):
        print("\n" + "-" * (self.ancho * 4 + 1))
        for f in range(self.alto):
            linea = "|"
            for c in range(self.ancho):
                celda = self.celdas[f][c]
                resaltar = (f == fila_ultima and c == col_ultima)

                if celda == Ficha.VACIA:
                    linea += "   |"
                elif celda == Ficha.CIRCULO:
                    if resaltar:
                        linea += " \033[32mO\033[0m |"
                    else:
                        linea += " \033[33mO\033[0m |"
                elif celda == Ficha.EQUIS:
                    if resaltar:
                        linea += " \033[32mX\033[0m |"
                    else:
                        linea += " \033[31mX\033[0m |"

            print(linea)
            print("-" * (self.ancho * 4 + 1))

    def columna_llena(self, col):
        return self.celdas[0][col] != Ficha.VACIA

    def colocar_ficha(self, ficha, col):
        for f in range(self.alto - 1, -1, -1):
            if self.celdas[f][col] == Ficha.VACIA:
                self.celdas[f][col] = ficha
                return f
        return -1

    def hay_casillas_libres(self):
        return any(Ficha.VACIA in fila for fila in self.celdas)

    def comprobar_gana(self, fila, columna, ficha, num_fichas):
        return (
            self._horizontal(fila, columna, ficha) >= num_fichas or
            self._vertical(fila, columna, ficha) >= num_fichas or
            self._diagonal(fila, columna, ficha) >= num_fichas
        )

    def _horizontal(self, fila, columna, ficha):
        contador = 1
        c = columna - 1
        while c >= 0 and self.celdas[fila][c] == ficha:
            contador += 1
            c -= 1

        c = columna + 1
        while c < self.ancho and self.celdas[fila][c] == ficha:
            contador += 1
            c += 1

        return contador

    def _vertical(self, fila, columna, ficha):
        contador = 1
        f = fila + 1
        while f < self.alto and self.celdas[f][columna] == ficha:
            contador += 1
            f += 1
        return contador

    def _diagonal(self, fila, columna, ficha):
        maximo = 1

        contador = 1
        f, c = fila + 1, columna + 1
        while f < self.alto and c < self.ancho and self.celdas[f][c] == ficha:
            contador += 1
            f += 1
            c += 1

        f, c = fila - 1, columna - 1
        while f >= 0 and c >= 0 and self.celdas[f][c] == ficha:
            contador += 1
            f -= 1
            c -= 1

        maximo = max(maximo, contador)

        contador = 1
        f, c = fila + 1, columna - 1
        while f < self.alto and c >= 0 and self.celdas[f][c] == ficha:
            contador += 1
            f += 1
            c -= 1

        f, c = fila - 1, columna + 1
        while f >= 0 and c < self.ancho and self.celdas[f][c] == ficha:
            contador += 1
            f -= 1
            c += 1

        maximo = max(maximo, contador)
        return maximo

    def simular_gana(self, columna, ficha, num_fichas):
        fila = self.colocar_ficha(ficha, columna)
        if fila == -1:
            return False

        gana = self.comprobar_gana(fila, columna, ficha, num_fichas)
        self.celdas[fila][columna] = Ficha.VACIA
        return gana

    def fichas_en_linea(self, columna, ficha):
        fila = self.colocar_ficha(ficha, columna)
        if fila == -1:
            return 0

        valor = max(
            self._horizontal(fila, columna, ficha),
            self._vertical(fila, columna, ficha),
            self._diagonal(fila, columna, ficha)
        )

        self.celdas[fila][columna] = Ficha.VACIA
        return valor
