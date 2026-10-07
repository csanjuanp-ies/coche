class Posicion:
    def __init__(self, longitud:float, latitud:float):
        self._longitud: float = longitud
        self._latitud: float = latitud

    def __str__(self):
        return f"({self._longitud}, {self._latitud})"

    @property
    def longitud(self) -> float:
        return self._longitud

    @longitud.setter
    def longitud(self, value: float):
        if -180.0 <= value <= 180-0:
            self._longitud = value
            return
        raise ValueError("La longitud debe estar entre -180 y 180")

    @property
    def latitud(self) -> float:
        return self._latitud

    @latitud.setter
    def latitud(self, value: float):
        if -90.0 <= value <= 90.0:
            self._latitud = value
            return
        raise ValueError("La latitud debe estar entre -90 y 90")
