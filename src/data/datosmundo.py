class DatosMundo:
    def __init__(self, izq:bool, der:bool, fre:bool):
        self.izquierda:bool = izq
        self.derecha:bool = der
        self.frente:bool = fre

    def all(self)->bool:
        return self.izquierda and self.derecha and self.frente
