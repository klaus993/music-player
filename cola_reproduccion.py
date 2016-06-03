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
        self.acciones_deshechas = Pila()
        self.actual = 0
        #self.ultima_accion = None
        #self.lista_canciones = lista_canciones

    def cancion_actual(self):
        """ Devuelve un objeto de clase Cancion que corresponde a la cancion actual, o None si no 
        hay canciones cargadas en la cola."""
        if self.lista_canciones.esta_vacia():
            return None
        return self.lista_canciones.get_elemento(self.actual)

    def cancion_siguiente(self):
        """ Devuelve un objeto de clase Cancion que corresponde a la cancion siguiente en la cola, 
        o None si no hay mas canciones."""
        if len(self.lista_canciones) < 1:
            return None
        self.actual += 1
        return self.lista_canciones.get_elemento(self.actual)

    def cancion_anterior(self):
        """ Devuelve un objeto de clase Cancion que corresponde a la cancion anterior en la cola, 
        o None si no hay canciones en la misma o la actual es la primera de la cola."""
        if len(self.lista_canciones) < 1:
            return None
        self.actual -= 1
        return self.lista_canciones.get_elemento(self.actual)

    def agregar_cancion(self, ruta_cancion):
        """ Agrega una Cancion a la cola a partir de su ruta. Devuelve True si se agrego 
        correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
        try:
            cancion = Cancion(ruta_cancion)
            self.lista_canciones.insert(cancion)
            self.acciones_tomadas.apilar((cancion, self.AGREGADA))
            return True
        except (TinyTagException, LookupError, OSError):
            return False

    def remover_cancion(self, ruta_cancion):
        """ Remueve una Cancion de la cola a partir de su ruta. Devuelve True si se removio 
        correctamente, False en caso contrario. Esta accion puede deshacerse y rehacerse."""
        try:
            cancion = Cancion(ruta_cancion)
            posicion = self.lista_canciones.index(cancion)
            self.lista_canciones.pop(posicion)
            self.acciones_tomadas.apilar((cancion, self.REMOVIDA))
            return True
        except (TinyTagException, LookupError, OSError) as e:
            print(str(e))
            return False

    def deshacer_modificacion(self):
        """ Deshace la ultima accion realizada. Devuelve True si pudo deshacerse, False en caso 
        contrario."""
        try:
            ultima_cancion, ultima_accion = self.acciones_tomadas.desapilar()
            if ultima_accion == self.AGREGADA:
                self.remover_cancion(ultima_cancion.obtener_ruta())
                self.acciones_deshechas.apilar((ultima_cancion, self.AGREGADA))
                return True
            self.agregar_cancion(ultima_cancion.obtener_ruta())
            self.acciones_deshechas.apilar((ultima_cancion, self.REMOVIDA))
            return True
        except (ValueError, IndexError):
            return False

    def rehacer_modificacion(self):
        """ Rehace la ultima accion que se deshizo. Devuelve True si pudo rehacerse, False en caso 
        contrario."""
        try:
            ultima_cancion, ultima_accion = self.acciones_deshechas.desapilar()
            if ultima_accion == self.AGREGADA:
                self.agregar_cancion(ultima_cancion.obtener_ruta())
                self.acciones_tomadas.apilar((ultima_cancion, self.AGREGADA))
                return True
            self.remover_cancion(ultima_cancion.obtener_ruta())
            self.acciones_tomadas.apilar((ultima_cancion, self.REMOVIDA))
            return True
        except (ValueError, IndexError):
            return False

    def obtener_n_siguientes(self, n_canciones):
        """ Devuelve una lista con las siguientes n canciones. Si en la cola de reproduccion 
        quedan menos canciones que las pedidas, la lista contendra menos elementos que los 
        pedidos."""
        if self.lista_canciones.esta_vacia():
            return None
        lista = []
        for i in range(n_canciones):
            try:
                lista.append(self.lista_canciones.get_elemento(self.actual + 1 + i))
            except IndexError:
                return lista
        return lista

    def __str__(self):
        return str(self.lista_canciones)
