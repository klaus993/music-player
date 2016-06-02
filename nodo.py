class _Nodo:
    """Clase que modela nodos de una lista enlazada"""
    def __init__(self, dato=None, prox=None, ant=None):
        self.dato = dato
        self.prox = prox
        self.ant = ant

    def __str__(self):
        return str(self.dato)

    def ver_lista(self):
        """Recorre todos los nodos a través de sus enlaces, mostrando sus contenidos."""
        nodo = self
        while nodo is not None:
            print(nodo)
            nodo = nodo.prox
