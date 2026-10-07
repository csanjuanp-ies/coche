"""
Representa elmundo real en una cuadrícula de tamaño fijo,
Por simplicidad aremos pruebas con tamaño de 10º
al pasar a producción, se reducirá a tamaño de 0,0001º
."""


class Mundo:
    """Representa el mundo del juego."""
    TAMAÑO_GRILL: int = 10 # nuestro mundo de 10º 36x18
    TOTAL_LONGITUD:int = 360 # longitud total del mundo
    TOTAL_LATITUD:int = 180 # latitud total del mundo

    def __init__(self):
        self.grid = [
            [0 for _ in range(self.TAMAÑO_GRILL)] for _ in range(self.TAMAÑO_GRILL)]
