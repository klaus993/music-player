import os
import sys

import pyglet
from ventana_reproductor import VentanaReproductor
from reproductor import Reproductor
from cola_reproduccion import ColaDeReproduccion, EXTENSIONES_ACEPTADAS
from cancion import Cancion
from lista_enlazada import ListaEnlazada

cancion1=Cancion("alice_in_chains_check_my_brain.mp3")
cancion2=Cancion("alice_in_chains_check_my_brain.mp3")
#colarepr=ColaDeReproduccion([cancion1, cancion2])
"""lista=ListaEnlazada()
lista.insert(cancion1)
lista.insert(cancion2)
print(lista.index(cancion1))"""
lista=ColaDeReproduccion([cancion1, cancion2])
print(lista.cancion_anterior())
