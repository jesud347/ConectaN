from Ficha import Ficha
from Tablero import Tablero
from Jugador import Jugador

class JuegoConectaN:
    def __init__(self):
        print("\nBienvenido al juego Conecta N\n")
        self.alto, self.ancho, self.num_fichas = self._pedir_tablero()
        self.tablero = Tablero(self.alto, self.ancho)
        self.jugadores = self._crear_jugadores()

    def _leer_entero(self, msg, minimo=None, maximo=None):
        while True:
            try:
                n = int(input(msg))
                if minimo is not None and n < minimo:
                    raise ValueError
                if maximo is not None and n > maximo:
                    raise ValueError
                return n
            except ValueError:
                print("Número inválido")

    def _pedir_tablero(self):
        alto = self._leer_entero("ALTO (mín 6): ", 6)
        ancho = self._leer_entero("ANCHO (mín 7): ", 7)
        max_f = max(alto, ancho)
        num_f = self._leer_entero(f"Fichas para ganar (4 - {max_f}): ", 4, max_f)
        return alto, ancho, num_f

    def _crear_jugadores(self):
        modo = self._leer_entero("(1) 2 Jugadores | (2) vs IA: ", 1, 2)
        nombre1 = input("Nombre jugador 1: ")

        j1 = Jugador(nombre1, Ficha.CIRCULO, es_ia=False, num_fichas=self.num_fichas)

        if modo == 1:
            nombre2 = input("Nombre jugador 2: ")
            j2 = Jugador(nombre2, Ficha.EQUIS, es_ia=False, num_fichas=self.num_fichas)
        else:
            nivel = self._leer_entero("Nivel IA (1 fácil, 2 difícil): ", 1, 2)
            j2 = Jugador("IA", Ficha.EQUIS, es_ia=True, nivel_ia=nivel, num_fichas=self.num_fichas)

        return [j1, j2]

    def jugar(self):
        turno = 0
        self.tablero.mostrar()

        while True:
            jugador = self.jugadores[turno]
            col = jugador.elegir_columna(self.tablero)

            fila = self.tablero.colocar_ficha(jugador.ficha, col)
            self.tablero.mostrar(fila, col)

            if self.tablero.comprobar_gana(fila, col, jugador.ficha, self.num_fichas):
                print(f"\nHA GANADO {jugador.nombre}\n")
                break

            if not self.tablero.hay_casillas_libres():
                print("\nEMPATE\n")
                break

            turno = 1 - turno

if __name__ == "__main__":
    juego = JuegoConectaN()
    juego.jugar()
