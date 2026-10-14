class DatosMundo:
    """
        El sensor de ultrasonidos buscará obstáculos en tres direcciones: 
        izquierda, derecha y frente, esta clase representa esos datos.
    """
    def __init__(self, izq:bool, der:bool, fre:bool):
        self.izquierda:bool = izq
        self.derecha:bool = der
        self.frente:bool = fre

    def all(self)->bool:
        return self.izquierda and self.derecha and self.frente

    def __str__(self) -> str:
        return f"(i:{self.izquierda}, c:{self.frente}, d:{self.derecha})"
