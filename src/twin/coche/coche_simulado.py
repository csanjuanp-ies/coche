from clases_datos.posicion import Posicion
from clases_datos.datosmundo import DatosMundo
from twin.coche.coche import Coche
import random
import math


class CocheSimulado(Coche):
    TAMAÑO_SALTO: int = 1

    def __init__(self, latitud:float, longitud:float, direccion: Coche.Direccion = Coche.Direccion.NORTE, simulacion:bool=False):
        super().__init__(latitud, longitud, direccion, True)   

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

    def _ejecutar_accion(self, accion: Coche.Accion) -> None:
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

    def _rotar_izquierda(self) -> None:
       self.direccion = Coche.Direccion.rotate_izq(self.direccion)

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
        return DatosMundo(False, True, True)


    def mover(self, llegada: Posicion, datos_mundo: DatosMundo) -> Coche.Accion:
        opcion: Coche.Accion = Coche.Accion.AVANZAR
        distancia: float = self._calcular_distancia(llegada)
        direccion: float = self._calcular_direccion(llegada, distancia)
        if datos_mundo.all() or distancia < 0 or direccion < 0:
            opcion = Coche.Accion.RETROCEDER
        else:
            opcion = random.choice([
                Coche.Accion.AVANZAR, 
                Coche.Accion.GIRAR_IZQUIERDA, 
                Coche.Accion.GIRAR_DERECHA, 
                Coche.Accion.RETROCEDER])

        self._ejecutar_accion(opcion)
        return opcion
