import os
from cancion import Cancion, TinyTagException
from cola import Cola
from pila import Pila
from lista_enlazada import ListaEnlazada


EXTENSIONES_ACEPTADAS = ("wav", "mp3", "flac", "ogg", "wma")


class ColaDeReproduccion:
    """Clase que representa la cola de reproduccion del reproductor. Permite agregar y remover 
    canciones, ademas de poder hacer y deshacer estas acciones. Las canciones se guardan en la 
    cola como objetos de clase Cancion."""

    AGREGADA = 1
    REMOVIDA = 0

    def __init__(self, lista_canciones=[]):
        """ Recibe una lista de objetos de clase Cancion con las canciones que se quieren 
        reproducir."""
        lista = ListaEnlazada()
        for cancion in lista_canciones:
            lista.insert(cancion)
        self.lista_canciones = lista
        self.acciones_tomadas = Pila()
        self.actual=0
        #self.ultima_accion = None
        #self.lista_canciones = lista_canciones


    def cancion_actual(self):
        """ Devuelve un objeto de clase Cancion que corresponde a la cancion actual, o None si no 
        hay canciones cargadas en la cola."""
        if self.lista_canciones.esta_vacia():
            return None
        #return self.cola_canciones.ver_primero()
        return self.lista_canciones.get_elemento(self.actual)

    def cancion_siguiente(self):
        """ Devuelve un objeto de clase Cancion que corresponde a la cancion siguiente en la cola, 
        o None si no hay mas canciones."""
        if self.lista_canciones.esta_vacia():
            return None
        return self.lista_canciones.get_elemento(self.actual+1)

    def cancion_anterior(self):
        """ Devuelve un objeto de clase Cancion que corresponde a la cancion anterior en la cola, 
        o None si no hay canciones en la misma o la actual es la primera de la cola."""
        #if self.lista_canciones.esta_vacia() or self.lista_canciones.ver_primero() == self.lista_canciones.ver_ultimo():
        if self.lista_canciones.esta_vacia():
            return None
        return self.lista_canciones.get_elemento(self.actual-1)

    def agregar_cancion(self, ruta_cancion):
        """ Agrega una Cancion a la cola a partir de su ruta. Devuelve True si se agrego 
        correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
        try:
            cancion = Cancion(ruta_cancion)
            self.lista_canciones.insert(cancion)
            #self.ultima_accion = self.AGREGADA
            self.acciones_tomadas.apilar((cancion, AGREGADA))
            return True
        except (TinyTagException, LookupError, OSError):
            return False

    def remover_cancion(self, ruta_cancion):
        """ Remueve una Cancion de la cola a partir de su ruta. Devuelve True si se removio 
        correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
        try:
            cancion = Cancion(ruta_cancion)
            #desencolada = self.cola_canciones.desencolar()
            #self._aux.apilar(desencolada)
            #self.ultima_accion = self.REMOVIDA
            posicion=self.lista_canciones.index(cancion)
            self.lista_canciones.pop(posicion)
            return True
        except (TinyTagException, LookupError, OSError):
            return False

    def deshacer_modificacion(self):
        """ Deshace la ultima accion realizada. Devuelve True si pudo deshacerse, False en caso 
        contrario."""
        raise NotImplementedError()

    def rehacer_modificacion(self):
        """ Rehace la ultima accion que se deshizo. Devuelve True si pudo rehacerse, False en caso 
        contrario."""
        raise NotImplementedError()

    def obtener_n_siguientes(self, n_canciones):
        """ Devuelve una lista con las siguientes n canciones. Si en la cola de reproduccion 
        quedan menos canciones que las pedidas, la lista contendra menos elementos que los 
        pedidos."""
        raise NotImplementedError()
