# Quispe Soliz Matias Fernando

# SIS420 - Inteligencia Artificial

import copy

class Tablero:
    def __init__(self):
        self.estado = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
        self.contador_jugador = 0
        self.contador_ordenador = 0

    def marcar_posicion(self, fila, columna, letra):
        self.estado[fila][columna] = letra
        if letra == 'O':
            self.contador_ordenador += 1
        else:
            self.contador_jugador += 1


    def imprimir_tablero(self):
        for i in range(3):
            print('-------------')
            for j in range(3):
                print(f'| {self.estado[i][j]} ', end='')
            print('|')
        print('-------------')

    def get_posiciones_vacias(self):
        posiciones_vacias = []
        for fila in range(3):
            for columna in range(3):
                if self.estado[fila][columna] == ' ':
                    posiciones_vacias.append((fila, columna))
        return posiciones_vacias
    
    def cantidad_marcaciones(self):
        print("Cantidad Marcaciones Jugador: " + str(self.contador_jugador))
        print("\nCantidad Marcaciones Ordenador: " + str(self.contador_ordenador))
    
    def hay_ganador(self):
        if self.contador_jugador < 4 and self.contador_ordenador < 4:
            return False

        secuencias_jugador = self.buscar_secuencias('X')
        secuencias_ordenador = self.buscar_secuencias('O')

        for secuencia in secuencias_jugador:
            if len(secuencia) >= 4:
                return True

        for secuencia in secuencias_ordenador:
            if len(secuencia) >= 4:
                return True

        return False
    
    # Determina el ganador
    def ganador(self):
        secuencias_jugador = self.buscar_secuencias('X')
        secuencias_ordenador = self.buscar_secuencias('O')

        if self.contador_jugador == 4 and self.contador_ordenador == 4:
            if len(secuencias_jugador) > len(secuencias_ordenador):
                print(jugador + " = " + str(len(secuencias_jugador)))
                print(ordenador + " = " + str(len(secuencias_ordenador)))
                print("Ganaste!")
            elif len(secuencias_ordenador) > len(secuencias_jugador):
                print(jugador + " = " + str(len(secuencias_jugador)))
                print(ordenador + " = " + str(len(secuencias_ordenador)))
                print("Perdiste :( Ganó la computadora.")
            else:
                print("Empate")


    def buscar_secuencias(self, letra):
        secuencias = []
        for fila in self.estado:
            secuencia_actual = []
            for columna in fila:
                if columna == letra:
                    secuencia_actual.append(columna)
                else:
                    if len(secuencia_actual) >= 2:
                        secuencias.append(secuencia_actual)
                    secuencia_actual = []
            if len(secuencia_actual) >= 2:
                secuencias.append(secuencia_actual)

        for columna in range(3):
            secuencia_actual = []
            for fila in range(3):
                if self.estado[fila][columna] == letra:
                    secuencia_actual.append(self.estado[fila][columna])
                else:
                    if len(secuencia_actual) >= 2:
                        secuencias.append(secuencia_actual)
                    secuencia_actual = []
            if len(secuencia_actual) >= 2:
                secuencias.append(secuencia_actual)

        return secuencias
    
    def terminar_juego(self):
        if self.contador_jugador == 4 and self.contador_ordenador == 4:
            return True
        else:
            return False


def minimax(tablero, es_turno_jugador, alpha, beta):
    if tablero.hay_ganador():
        if es_turno_jugador:
            return -10, None
        else:
            return 10, None

    posiciones_vacias = tablero.get_posiciones_vacias()

    if tablero.contador_jugador == 4 and tablero.contador_ordenador == 4:
        secuencias_jugador = tablero.buscar_secuencias('X')
        secuencias_ordenador = tablero.buscar_secuencias('O')

        mejor_secuencia_jugador = max(secuencias_jugador, key=len, default=[])
        mejor_secuencia_ordenador = max(secuencias_ordenador, key=len, default=[])

        if len(mejor_secuencia_jugador) > len(mejor_secuencia_ordenador):
            return -10, None
        elif len(mejor_secuencia_jugador) < len(mejor_secuencia_ordenador):
            return 10, None
        else:
            return 0, None

    if es_turno_jugador:
        mejor_valor = float('-inf')
        mejor_posicion = None
        for fila, columna in posiciones_vacias:
            tablero_aux = copy.deepcopy(tablero)
            tablero_aux.marcar_posicion(fila, columna, 'X')
            valor_actual, _ = minimax(tablero_aux, False, alpha, beta)
            if valor_actual > mejor_valor:
                mejor_valor = valor_actual
                mejor_posicion = (fila, columna)
            alpha = max(alpha, mejor_valor)
            if beta <= alpha:
                break
        return mejor_valor, mejor_posicion

    else:
        mejor_valor = float('inf')
        mejor_posicion = None
        for fila, columna in posiciones_vacias:
            tablero_aux = copy.deepcopy(tablero)
            tablero_aux.marcar_posicion(fila, columna, 'O')
            valor_actual, _ = minimax(tablero_aux, True, alpha, beta)
            if valor_actual < mejor_valor:
                mejor_valor = valor_actual
                mejor_posicion = (fila, columna)
            beta = min(beta, mejor_valor)
            if beta <= alpha:
                break
        return mejor_valor, mejor_posicion
    
if __name__ == "__main__":
    tablero = Tablero()
    print("¡Bienvenido al juego de marcas!")
    jugador = input("¿Quieres jugar como 'O' o como 'X'? ").upper()
    while jugador != "O" and jugador != "X":
        jugador = input("Por favor, elige 'O' o 'X': ").upper()

    if jugador == "O":
        ordenador = "X"
    else:
        ordenador = "O"

    print(f"Juegas como '{jugador}' y el ordenador juega como '{ordenador}'")

    # Determinar quién comienza
    jugador_comienza = input("¿Quieres comenzar tú? (S/N): ")
    if jugador_comienza.lower() == 's':
        es_turno_jugador = True
    else:
        es_turno_jugador = False


    while not tablero.terminar_juego():
        if es_turno_jugador:
            print("\nEs tu turno.\n")
            tablero.imprimir_tablero()
            fila = int(input("Elige una fila (1, 2, 3): "))
            columna = int(input("Elige una columna (1, 2, 3): "))
            while tablero.estado[fila-1][columna-1] != ' ':
                print("Esa posición ya está ocupada. Elige otra.")
                fila = int(input("Elige una fila (1, 2, 3): "))
                columna = int(input("Elige una columna (1, 2, 3): "))

            tablero.marcar_posicion(fila - 1, columna - 1, jugador)
            es_turno_jugador = False
        else:
            print("\nEs el turno del ordenador.\n")
            tablero.imprimir_tablero()
            _, (fila, columna) = minimax(tablero, False, float('-inf'), float('inf'))
            tablero.marcar_posicion(fila, columna, ordenador)
            es_turno_jugador = True

    print("***  Juego Finalizado  ***")
    tablero.imprimir_tablero()
    tablero.ganador()
