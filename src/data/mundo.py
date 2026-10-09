"""
Representa elmundo real en una cuadrícula de tamaño fijo,
Por simplicidad aremos pruebas con tamaño de 10º
al pasar a producción, se reducirá a tamaño de 0,0001º
."""
from src.data.coche import Coche
from src.data.posicion import Posicion
from src.data.datosmundo import DatosMundo
import random


class Mundo:
    """Representa el mundo del juego."""
    TAMAÑO_GRILL: int = 10 # nuestro mundo de 10º 36x18
    TOTAL_LONGITUD:int = 360 # longitud total del mundo  # E o W
    TOTAL_LATITUD:int = 180 # latitud total del mundo N o S

    def __init__(self, simulado:bool = False, visualiazar_mapa:bool = True, visualizar_datos:bool = True):
        self._simulacion = simulado
        self._visualizar_mapa = visualiazar_mapa
        self._visualizar_datos = visualizar_datos
        # coche
        self.inicializar_datos()

        if self._simulacion:
            self._inicializar_simulacion()
            self.grid[int(self._coche.posicion.latitud)][int(self._coche.posicion.longitud)] = str(self._coche)

    def __str__(self):
        return f"Coche en {self._coche.posicion} con destino {self.destino}"

    def inicializar_datos(self):
        direccion: Coche.Direccion = random.choice(list(Coche.Direccion))
        lon_ini: int = random.randint(0, self.TOTAL_LONGITUD // self.TAMAÑO_GRILL - 1)
        lat_ini: int = random.randint(0, self.TOTAL_LATITUD // self.TAMAÑO_GRILL - 1)
        self._coche: Coche = Coche(lat_ini, lon_ini, direccion, self._simulacion)
        # destino
        lon_ini: int = random.randint(0, self.TOTAL_LONGITUD // self.TAMAÑO_GRILL - 1)
        lat_ini: int = random.randint(0, self.TOTAL_LATITUD // self.TAMAÑO_GRILL - 1)
        self.destino: Posicion = Posicion(lat_ini, lon_ini)
        
    def _inicializar_simulacion(self):
       self.grid = [
            [" " for _ in range(self.TOTAL_LONGITUD // self.TAMAÑO_GRILL)] 
                for _ in range(self.TOTAL_LATITUD // self.TAMAÑO_GRILL)
            ]

    def _leer_mundo(self) -> DatosMundo:
        # TODO: Implementar la lógica para leer el mundo real y devolver los datos del mundo
        return DatosMundo(False, True, True)

    def _dibujar_mundo(self):
        if not self._visualizar_mapa:
            return
        for lat in range(len(self.grid)):
            print("|", end="")
            for lon in range(len(self.grid[lat])):
                print(f"{self.grid[lat][lon]}", end="|")
            print(" ")

    def _resituar_coche(self):
        lat:int = int(self._coche.posicion.latitud)
        lon:int = int(self._coche.posicion.longitud)

        if lon < 0:
            lon = 35
        elif lon >= 36:
            lon = 0
        if lat < 0:
            lat = 17
        elif lat >= 18:
            lat = 0

        self._coche.posicion.latitud = lat
        self._coche.posicion.longitud = lon

    def run(self) -> int:
        """Inicia la simulación del mundo."""
        num_iteraciones: int = 0
        if self._simulacion:
            self._dibujar_mundo()
            fin: bool = False
            while not fin: # for _ in range(10): #  
                datos_mundo: DatosMundo = self._leer_mundo()
                self.grid[int(self._coche.posicion.latitud)][int(self._coche.posicion.longitud)] = " "
                if self._visualizar_datos:
                    print("old:", self._coche.log()) 
                accion: Coche.Accion = self._coche.mover(self.destino, datos_mundo)
                if self._visualizar_datos:
                    print(accion)
                self._resituar_coche()  # en la simulación el origen 0,0 arriba izquierda y máx de 35,17
                if self._visualizar_datos:
                    print("new:", self._coche.log())
                    print("destino:", self.destino) 
                self.grid[int(self._coche.posicion.latitud)][int(self._coche.posicion.longitud)] = str(self._coche)
                fin = self._coche.posicion == self.destino
                if self._visualizar_datos:
                    print("fin:", fin)
                self._dibujar_mundo()
                num_iteraciones += 1
            print(f"Simulación finalizada en {num_iteraciones} iteraciones.")
            return num_iteraciones
        return 0
