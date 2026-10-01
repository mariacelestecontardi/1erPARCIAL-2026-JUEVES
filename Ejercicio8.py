class Nodo:
    def __init__(self, dato, sig=None):
        self._elem = dato
        self._nxt = sig

    def obtener_dato(self):
        return self._elem

    def obtener_siguiente(self):
        return self.__nxt

    def cambiar_siguiente(self, sig):
        self.__nxt = sig


class ListaEnlazada:
    def __init__(self):
        self.header = Nodo(0)

    def append(self, dato):
        nuevo_nodo = Nodo(dato)
        actual = self.header

        while actual.obtener_siguiente() is not None:
            actual = actual.obtener_siguiente()

        actual.cambiar_siguiente(nuevo_nodo)

    def __iter__(self):
        actual = self.header.obtener_siguiente()

        while actual is not None: 
            yield actual.obtener_dato()
            actual = actual.obtener_siguiente()

    