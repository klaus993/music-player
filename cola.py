from nodo import _Nodo


class _IteradorCola:

    def __init__(self, prim):
        self.actual = prim

    def __next__(self):
        if self.actual is None:
            raise StopIteration()
        dato = self.actual.dato
        self.actual = self.actual.prox
        return dato


class Cola:

    def __init__(self):
        self.prim = None
        self.ult = None
        self.len = 0

    def __str__(self):
        result = '['
        node = self.prim
        if node is not None:
            result += str(node.dato)
            node = node.prox
            while node is not None:
                result += ', ' + str(node.dato)
                node = node.prox
        result += ']'
        return result

    def __iter__(self):
        return _IteradorCola(self.prim)

    def esta_vacia(self):
        return self.prim is None

    def encolar(self, dato):
        nodo = _Nodo(dato)
        if self.esta_vacia():
            self.prim = nodo
        else:
            self.ult.prox = nodo
        self.ult = nodo

    def desencolar(self):
        if self.esta_vacia():
            raise ValueError('La cola está vacía.')
        dato = self.prim.dato
        self.prim = self.prim.prox
        if not self.prim:
            self.ult = None
        return dato

    def ver_primero(self):
        return self.prim.dato
