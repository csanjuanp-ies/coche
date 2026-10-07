from src.data.posicion import Posicion
from src.data.datosmundo import DatosMundo
from enum import Enum
import random


class Coche:
    
    class Direccion(Enum):
        NORTE = 0
        ESTE = 90
        SUR = 180
        OESTE = 270

    class Accion(Enum):
        AVANZAR = 0
        GIRAR_IZQUIERDA = 1
        GIRAR_DERECHA = 2
        RETROCEDER = 3

    def __init__(self, ini_x:float, ini_y:float, direccion: Direccion = Direccion.NORTE):
        self.posicion: Posicion = Posicion(ini_x, ini_y) 
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

    def log(self) -> str:
        return f"Coche en {self.posicion} mirando hacia {self}"


    def avanzar(self, estoy: Posicion, llegada: Posicion, datos_mundo: DatosMundo) -> Accion:
        return random.choice([
            Coche.Accion.AVANZAR, 
            Coche.Accion.GIRAR_IZQUIERDA, 
            Coche.Accion.GIRAR_DERECHA, 
            Coche.Accion.RETROCEDER])
