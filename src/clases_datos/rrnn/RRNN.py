from abc import ABCMeta, abstractmethod
from clases_datos.datosmundo import DatosMundo
from twin.coche.coche import Coche
from clases_datos.posicion import Posicion


class RRNN(metaclass=ABCMeta):
    """
        Clase abstracta que define la interfaz de una red neuronal 
        para el control del coche.
    """
    @abstractmethod
    def run(self,
                actual:Posicion,  # longitud, latitud
                destino:Posicion,  # longitud, latitud
                datos_mundo:DatosMundo,  # izquierda, derecha, frente
                direccion:float,
                distancia:float) -> Coche.Accion:
        pass
