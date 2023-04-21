# Quispe Soliz Matias Fernando

# SIS420 - Inteligencia Artificial

from collections import deque

class Nodo:
    def __init__(self, estado, hijo=None):
        self.estado = estado
        self.hijo = []
        self.padre = None
        self.accion = None
        self.acciones = None
        self.costo = None
        self.set_hijo(hijo)

    def set_estado(self, estado):
        self.estado = estado

    def get_estado(self):
        return self.estado

    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijo.append(hijo)
            if self.hijo is not None:
                for h in self.hijo:
                    h.padre = self

    def get_hijo(self):
        return self.hijo

    def set_padre(self, padre):
        self.padre = padre

    def get_padre(self):
        return self.padre

    def set_accion(self, accion):
        self.accion = accion

    def get_accion(self):
        return self.accion

    def set_acciones(self, acciones):
        self.acciones = acciones

    def get_acciones(self):
        return self.acciones

    def set_costo(self, costo):
        self.costo = costo

    def get_costo(self):
        return self.costo


class Posicion(Nodo):
    def __init__(self, fila, columna, camino, hijo=None):
        estado = {'fila': fila, 'columna': columna, 'camino': camino}
        super().__init__(estado, hijo)

    def get_fila(self):
        return self.estado['fila']

    def get_columna(self):
        return self.estado['columna']

    def get_camino(self):
        return self.estado['camino']

    def __str__(self):
        return str(self.get_estado())


def encontrar_salida(laberinto):
    filas = len(laberinto)
    columnas = len(laberinto[0])
    visitado = [[False for _ in range(columnas)] for _ in range(filas)]
    cola = deque()
    salida_encontrada = None
    for fila in range(filas):
        for columna in range(columnas):
            if laberinto[fila][columna] == 'E':
                cola.append(Posicion(fila, columna, [(fila, columna)]))
                visitado[fila][columna] = True
            elif laberinto[fila][columna] in ['S1', 'S2', 'S3']:
                if not salida_encontrada:
                    salida_encontrada = laberinto[fila][columna]
    while cola:
        pos = cola.popleft()
        fila, columna = pos.get_fila(), pos.get_columna()
        if laberinto[fila][columna] in ['S1', 'S2', 'S3']:
            return pos.get_camino(), salida_encontrada
        for df, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nueva_fila, nueva_columna = fila + df, columna + dc
            if (0 <= nueva_fila < filas and 0 <= nueva_columna < columnas
                    and not visitado[nueva_fila][nueva_columna]
                    and laberinto[nueva_fila][nueva_columna] != '#'):
                visitado[nueva_fila][nueva_columna] = True
                nuevo_camino = pos.get_camino() + [(nueva_fila, nueva_columna)]
                cola.append(Posicion(nueva_fila, nueva_columna, nuevo_camino))


laberinto = [['E', ' ', ' ', ' ', '#', ' ', '#', '#', ' ', ' '],
             [' ', '#', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
             [' ', '#', ' ', ' ', '#', ' ', ' ', '#', ' ', '#'],
             ['#', ' ', ' ', ' ', '#', ' ', ' ', ' ', ' ', '#'],
             [' ', ' ', ' ', ' ', '#', '#', ' ', '#', ' ', ' '],
             [' ', '#', '#', ' ', ' ', '#', ' ', ' ', ' ', 'S3'],
             [' ', '#', ' ', ' ', ' ', ' ', ' ', ' ', ' ', '#'],
             [' ', '#', ' ', '#', '#', '#', '#', '#', ' ', '#'],
             [' ', ' ', ' ', ' ', ' ', ' ', ' ', '#', ' ', ' '],
             ['#', ' ', ' ', 'S1', '#', '#', '#', ' ', ' ', 'S2']
             ]

camino, salida_encontrada = encontrar_salida(laberinto)
print("Camino encontrado:", camino)
print('Recorrido del laberinto')


for posicion in camino:
    fila, columna = posicion
    laberinto[fila][columna] = 'x'

for fila in range(len(laberinto)):
    print(laberinto[fila])
