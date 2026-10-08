class Posicion:
    MAX_LONGITUD: float = 180.0
    MIN_LONGITUD: float = -180.0
    MAX_LATITUD: float = 90.0
    MIN_LATITUD: float = -90.0
    
    def __init__(self, latitud:float, longitud:float):
        self._longitud: float = longitud  # E o W  360º  x
        self._latitud: float = latitud  # N o S  180º  y


    def __str__(self):
        return f"({self._longitud}, {self._latitud})"

    @property
    def longitud(self) -> float:
        return self._longitud

    @longitud.setter
    def longitud(self, value: float):
        if -180.0 < value < 180.0:
            self._longitud = value
        elif value >= 180.0:
            self._longitud = 180.0
        elif value <= -180.0:
            self._longitud = - 180.0

    @property
    def latitud(self) -> float:
        return self._latitud
    
    @latitud.setter
    def latitud(self, value: float):
        if -90.0 < value < 90.0:
            self._latitud = value
        elif value >= 90.0:
            self._latitud = 90.0
        elif value <= -90.0:
            self._latitud = -90.0

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Posicion):
            return NotImplemented
        return self.latitud == other.latitud and self.longitud == other.longitud
