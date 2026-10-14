"""
    Representa elmundo real en una cuadrícula de tamaño fijo,
    Por simplicidad aremos pruebas con tamaño de 10º
    al pasar a producción, se reducirá a tamaño de 0,0001
."""
from twin.coche.coche import Coche
from twin.coche.coche_simulado import CocheSimulado
from twin.coche.coche_real import CocheReal
from clases_datos.posicion import Posicion
from clases_datos.datosmundo import DatosMundo
import random


class Mundo:
    TAMAÑO_GRILL: int = 10 # nuestro mundo de 10º 36x18
    TOTAL_LONGITUD:int = 360 # longitud total del mundo  # E o W
    TOTAL_LATITUD:int = 180 # latitud total del mundo N o S

    def __init__(self):
        self._simulacion = False  # El mundo se utiliza para entrenar la RRNN
        self._visualizar_mapa = False  # Visualizar el mapa del mundo
        self._visualizar_datos = False  # Visualizar los datos del coche y del mundo
        self._visualizar_ruta = False  # Visualizar la ruta del coche
        self.inicializar_datos()

    def __str__(self):
        return f"Coche en {self._coche.posicion} con destino {self.destino}"

    def _inicializar_grid(self):
       """
         Inicializa la cuadrícula del mundo con espacios vacíos.
         Se utiliza cuando hay una simulación
       """
       self.grid = [
            [" " for _ in range(self.TOTAL_LONGITUD // self.TAMAÑO_GRILL)] 
                for _ in range(self.TOTAL_LATITUD // self.TAMAÑO_GRILL)
            ]

    def _leer_mundo(self) -> DatosMundo:
        return self._coche.datos_mundo()

    def _dibujar_mundo(self):
        if not self._visualizar_mapa:
            return
        for lat in range(len(self.grid)):
            print("|", end="")
            for lon in range(len(self.grid[lat])):
                print(f"{self.grid[lat][lon]}", end="|")
            print(" ")
        print("*"*80)

    def _resituar_coche_en_simulacion(self):
        """
            Cuando desplazamos el coche, si en modo simulación se sale del mapa, 
            lo resituamos en el lado contrario.
        """
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

    # Patrón builder para configurar el mundo
    def hacer_simulado(self):
        self._simulacion = True
        return self

    def hacer_visualizar_mapa(self):
        self._visualizar_mapa = True
        return self

    def hacer_visualizar_datos(self):
        self._visualizar_datos = True
        return self

    def hacer_visualizar_ruta(self):
        self._visualizar_ruta = True
        return self

    def inicializar_datos(self):
        # Patrón factoria para crear el coche según el tipo de mundo
        if self._simulacion:
            self._inicializar_grid()
            try: 
                # Si pedimos recrear condiciones borra la posición anterior del coche en el grid
                self.grid[int(self._coche.posicion.latitud)][int(self._coche.posicion.longitud)] = " "
            except:
                pass
            # origen
            direccion: Coche.Direccion = random.choice(list(Coche.Direccion))
            lon_ini: int = random.randint(0, self.TOTAL_LONGITUD // self.TAMAÑO_GRILL - 1)
            lat_ini: int = random.randint(0, self.TOTAL_LATITUD // self.TAMAÑO_GRILL - 1)
            self._coche: Coche = CocheSimulado(lat_ini, lon_ini, direccion, self._simulacion)
            # destino
            lon_ini: int = random.randint(0, self.TOTAL_LONGITUD // self.TAMAÑO_GRILL - 1)
            lat_ini: int = random.randint(0, self.TOTAL_LATITUD // self.TAMAÑO_GRILL - 1)
            self.destino: Posicion = Posicion(lat_ini, lon_ini)
            # Posicionamos en el Grid el coche según la dirección correspondiente
            self.grid[int(self._coche.posicion.latitud)][int(self._coche.posicion.longitud)] = str(self._coche)
        else:
            # Si no es simulación el coche coge datos del GPS (False último parámetro)
            self._coche: Coche = CocheReal(0,0, Coche.Direccion.NORTE, False)
            # Poner datos destino HARDCode
            self.destino: Posicion = Posicion(0,0)
        

    def run(self) -> int:
        """
            Inicia la simulación del mundo.
        """
        num_iteraciones: int = 0
        if self._simulacion:
            self._dibujar_mundo()
            fin: bool = False
            while not fin: # for _ in range(10): #  
                datos_mundo: DatosMundo = self._leer_mundo()

                # Log por pantalla
                if not self._visualizar_ruta:
                    # Si hay que visulizar la ruta no se borran los datos del movimiento anterior
                    self.grid[int(self._coche.posicion.latitud)][int(self._coche.posicion.longitud)] = " "
                if self._visualizar_datos:
                    print("old:", self._coche.log()) 

                accion: Coche.Accion = self._coche.mover(self.destino, datos_mundo)

                # Log por pantalla
                if self._visualizar_datos:
                    print("accion:", accion)
                    print("Datos mundo:", datos_mundo)
                
                self._resituar_coche_en_simulacion()  # en la simulación el origen 0,0 arriba izquierda y máx de 35,17

                # Log por pantalla
                if self._visualizar_datos:
                    print("new:", self._coche.log())
                    print("destino:", self.destino) 
                
                self.grid[int(self._coche.posicion.latitud)][int(self._coche.posicion.longitud)] = str(self._coche)
                
                fin = self._coche.posicion == self.destino

                # Log por pantalla
                if self._visualizar_datos:
                    print("fin:", fin)
                if not self._visualizar_ruta:
                    self._dibujar_mundo()
                
                num_iteraciones += 1

            # Hemos llegado al fin, lo marcamos en el grid    
            self.grid[int(self.destino.latitud)][int(self.destino.longitud)] = "X"
            
            # Log por pantalla
            if self._visualizar_ruta:
                self._dibujar_mundo()
            print(f"Simulación finalizada en {num_iteraciones} iteraciones.")

            return num_iteraciones
        return -1  # Indica que no se ha ejecutado la simulación
