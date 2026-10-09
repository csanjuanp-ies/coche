from data.posicion import Posicion
from data.datosmundo import DatosMundo
from enum import Enum
from typing import Self
import random
import math


class Coche:
    TAMAÑO_SALTO: int = 1 # igual que el mundo debe ser 1 para simular 0.0001 para real
    
    class Direccion(Enum):
        NORTE = 0
        ESTE = 1
        SUR = 2
        OESTE = 3

        @classmethod
        def rotate_izq(cls, dir: Self):
            return cls((dir.value + 1) % 4)

        @classmethod
        def rotate_der(cls, dir: Self):
            return cls((dir.value - 1) % 4)


    class Accion(Enum):
        AVANZAR = 0
        GIRAR_IZQUIERDA = 1
        GIRAR_DERECHA = 2
        RETROCEDER = 3


    def __init__(self, latitud:float, longitud:float, direccion: Direccion = Direccion.NORTE, simulacion:bool=False):
        if simulacion:
            self.posicion: Posicion = Posicion(latitud, longitud) 
            self.direccion: Coche.Direccion = direccion
            self.simulacion: bool = simulacion 
        else:
            # Leer datos del GPS y establecer lo siguiente
            self.posicion: Posicion = Posicion(0, 0) 
            self.direccion: Coche.Direccion = Coche.Direccion.NORTE
            self.simulacion: bool = False 

    def __str__(self) -> str:
        char_direccion: str = ""

        match self.direccion:
            case Coche.Direccion.NORTE:
                char_direccion = "\U00002191"
            case Coche.Direccion.ESTE:
                char_direccion = "\U00002190"
            case Coche.Direccion.SUR:
                char_direccion = "\U00002193"
            case Coche.Direccion.OESTE:
                char_direccion = "\U00002192"

        return f"{char_direccion}"

    def _ejecutar_accion(self, accion: Accion) -> None:
        match accion:
            case Coche.Accion.AVANZAR:
               self._avanzar()
            case Coche.Accion.RETROCEDER:
               self._retroceder()
            case Coche.Accion.GIRAR_IZQUIERDA:
                self._rotar_izquierda()
            case Coche.Accion.GIRAR_DERECHA:
                self._rotar_derecha()
                
    def _rotar_derecha(self) -> None:
       self.direccion = Coche.Direccion.rotate_der(self.direccion)
       # TODO: girar 1sg motores para rotar 90º

    def _rotar_izquierda(self) -> None:
       self.direccion = Coche.Direccion.rotate_izq(self.direccion)
       # TODO: girar 1sg motores para rotar -90º

    def _avanzar(self) -> None:
        # habría que tener en cuenta la dirección para las posiciones extremas 
        # del mundo, pero como es una simulación no lo vamos a hacer
        match self.direccion:
            case Coche.Direccion.NORTE:
                self.posicion.latitud -= self.TAMAÑO_SALTO
            case Coche.Direccion.OESTE:
                self.posicion.longitud += self.TAMAÑO_SALTO
            case Coche.Direccion.SUR:
                self.posicion.latitud += self.TAMAÑO_SALTO
            case Coche.Direccion.ESTE:
                self.posicion.longitud -= self.TAMAÑO_SALTO
        # TODO: avanzar motores 1sg

    def _retroceder(self) -> None:
        # habría que tener en cuenta la dirección para las posiciones extremas 
        # del mundo, pero como es una simulación no lo vamos a hacer
        match self.direccion:
            case Coche.Direccion.NORTE:
                self.posicion.latitud += self.TAMAÑO_SALTO
            case Coche.Direccion.OESTE:
                self.posicion.longitud -= self.TAMAÑO_SALTO
            case Coche.Direccion.SUR:
                self.posicion.latitud -= self.TAMAÑO_SALTO
            case Coche.Direccion.ESTE:
                self.posicion.longitud += self.TAMAÑO_SALTO
        # TODO: retroceder motores 1sg


    def _calcular_distancia(self, llegada: Posicion) -> float:
        return ((llegada.longitud - self.posicion.longitud)**2 
                + (llegada.latitud - self.posicion.latitud)**2)**0.5 

    def _calcular_direccion(self, llegada: Posicion, distancia: float) -> float:
        rx: float = llegada.longitud - self.posicion.longitud
        ry: float = llegada.longitud - self.posicion.latitud 
        s1:float = math.acos(rx / distancia)
        s2:float = 360 - s1
        if rx>0 and ry>0:
            return s1 if 0<= s1 <= 90 else s2
        elif rx>0 and ry<0:
            return s1 if 270<= s1 <= 360 else s2
        elif rx<0 and ry>0:
            return s1 if 90<= s1 <= 180 else s2
        elif rx<0 and ry<0:
            return s1 if 180<= s1 <= 270 else s2
        return 0

    def log(self) -> str:
        return f"Coche en {self.posicion} mirando hacia {self}"

    def datos_mundo(self) -> DatosMundo:
        if self.simulacion:
            return DatosMundo(False, True, True)
        # TODO: Leer datos con el sensor de ultrasonidos
        return DatosMundo(True, True, True)

    def mover(self, llegada: Posicion, datos_mundo: DatosMundo) -> Coche.Accion:
       
        opcion: Coche.Accion = Coche.Accion.AVANZAR
        distancia: float = self._calcular_distancia(llegada)
        direccion: float = self._calcular_direccion(llegada, distancia)
        if self.simulacion: 
            if datos_mundo.all() or distancia < 0 or direccion < 0:
                opcion = Coche.Accion.RETROCEDER
            else:
                opcion = random.choice([
                    Coche.Accion.AVANZAR, 
                    Coche.Accion.GIRAR_IZQUIERDA, 
                    Coche.Accion.GIRAR_DERECHA, 
                    Coche.Accion.RETROCEDER])
        else:
             # TODO: llamar a la IA pasando los datos del mundo y
             # la posición de llegada y que devuelva la acción a ejecutar
            pass # 
        self._ejecutar_accion(opcion)
        # TODO: leer nueva posición del GPS y actualizar self.posicion
        return opcion
