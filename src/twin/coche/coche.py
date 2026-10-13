from clases_datos.posicion import Posicion
from clases_datos.datosmundo import DatosMundo
from enum import Enum
from typing import Self
from abc import ABCMeta, abstractmethod


class Coche(metaclass=ABCMeta):
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
        self.posicion: Posicion = Posicion(latitud, longitud) 
        self.direccion: Coche.Direccion = direccion
        self.simulacion: bool = simulacion 

    @abstractmethod
    def __str__(self) -> str:
        pass

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
                
    @abstractmethod
    def _rotar_derecha(self) -> None:
       pass

    @abstractmethod
    def _rotar_izquierda(self) -> None:
       pass

    @abstractmethod
    def _avanzar(self) -> None:
        pass

    @abstractmethod
    def _retroceder(self) -> None:
        pass

    @abstractmethod
    def _calcular_distancia(self, llegada: Posicion) -> float:
        pass

    @abstractmethod
    def _calcular_direccion(self, llegada: Posicion, distancia: float) -> float:
        pass

    @abstractmethod
    def log(self) -> str:
        pass

    @abstractmethod
    def datos_mundo(self) -> DatosMundo:
        pass

    @abstractmethod
    def mover(self, llegada: Posicion, datos_mundo: DatosMundo) -> Coche.Accion:
      pass
