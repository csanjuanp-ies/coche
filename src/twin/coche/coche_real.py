from clases_datos.posicion import Posicion
from clases_datos.datos_mundo import DatosMundo
from twin.coche.coche import Coche
from clases_datos.rrnn.rrnn import RRNN
import math


class CocheReal(Coche):
    TAMAÑO_SALTO: float = 0.0001

    def __init__(self, 
                 latitud:float, 
                 longitud:float, 
                 direccion: Coche.Direccion = Coche.Direccion.NORTE, 
                 simulacion:bool=False):
            super().__init__(0, 0, direccion, False)
            self._rrnn: None| RRNN = None

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

    def set_rrnn(self, rrnn: RRNN) -> None:
        self._rrnn = rrnn

    def _rotar_derecha(self) -> None:
       self.direccion = Coche.Direccion.rotate_der(self.direccion)
       # TODO: girar motores para rotar 90º

    def _rotar_izquierda(self) -> None:
       self.direccion = Coche.Direccion.rotate_izq(self.direccion)
       # TODO: girar motores para rotar -90º

    def _avanzar(self) -> None:
        pass
        # TODO: avanzar motores 1sg

    def _retroceder(self) -> None:
        pass
        # TODO: retroceder motores 1sg


    def _calcular_distancia(self, destino: Posicion) -> float:
        return ((destino.longitud - self.posicion.longitud)**2 
                + (destino.latitud - self.posicion.latitud)**2)**0.5 

    def _calcular_direccion(self, destino: Posicion, distancia: float) -> float:
        rx: float = destino.longitud - self.posicion.longitud
        ry: float = destino.longitud - self.posicion.latitud
        if distancia == 0:
           return 0 
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
        # TODO: Leer datos con el sensor de ultrasonidos
        return DatosMundo(True, True, True)

    def mover(self, destino: Posicion, datos_mundo: DatosMundo) -> Coche.Accion:
        opcion: Coche.Accion = Coche.Accion.AVANZAR
        distancia: float = self._calcular_distancia(destino)
        direccion: float = self._calcular_direccion(destino, distancia)

        if not self._rrnn:
            raise ValueError("No se ha establecido la función rrnn")
        opcion = self._rrnn.run(self.posicion, destino, datos_mundo, direccion, distancia)

        self._ejecutar_accion(opcion)
        # TODO: leer nueva posición del GPS y actualizar self.posicion
        return opcion
