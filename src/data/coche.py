from src.data.posicion import Posicion
from src.data.datosmundo import DatosMundo
from enum import Enum
from typing import Self
import random


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


    def __init__(self, latitud:float, longitud:float, direccion: Direccion = Direccion.NORTE):
        self.posicion: Posicion = Posicion(latitud, longitud) 
        self.direccion: Coche.Direccion = direccion 

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
       # TODO: firar 1sg motores para rotar 90º

    def _rotar_izquierda(self) -> None:
       self.direccion = Coche.Direccion.rotate_izq(self.direccion)
       # TODO: firar 1sg motores para rotar -90º

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
        # TODO: ºavanzar motores 1sg

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

    def log(self) -> str:
        return f"Coche en {self.posicion} mirando hacia {self}"

    def mover(self, llegada: Posicion, datos_mundo: DatosMundo) -> Coche.Accion:
        # TODO: llamar a la IA pasando los datos del mundo y 
        # la posición de llegada y que devuelva la acción a ejecutar 
        opcion: Coche.Accion = Coche.Accion.AVANZAR
        if datos_mundo.all():
            opcion = Coche.Accion.RETROCEDER
        else:
            opcion = random.choice([
                Coche.Accion.AVANZAR, 
                Coche.Accion.GIRAR_IZQUIERDA, 
                Coche.Accion.GIRAR_DERECHA, 
                Coche.Accion.RETROCEDER])

        self._ejecutar_accion(opcion)

        return opcion
