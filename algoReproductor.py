#!/usr/bin/python3

import os
import sys

import pyglet
from ventana_reproductor import VentanaReproductor
from reproductor import Reproductor
from cola_reproduccion import ColaDeReproduccion, EXTENSIONES_ACEPTADAS


def agregar_canciones(cola, ruta_directorio):
    """ Agrega a la cola las canciones que se encuentran en el directorio y en los directorios
    que se encuentran en el, recursivamente. Las extensiones aceptadas son las que se listan en 
    ColaDeReproduccion."""
    directorio_actual = os.listdir(ruta_directorio)
    if not directorio_actual:       # verifica que no esté vacío el directorio actual
        return
    for archivo in directorio_actual:
        if os.path.isdir('{}/{}'.format(ruta_directorio, archivo)):
            agregar_canciones(cola, '{}/{}'.format(ruta_directorio, archivo))
        if archivo.endswith(EXTENSIONES_ACEPTADAS):
            cola.agregar_cancion('{}/{}'.format(ruta_directorio, archivo))


def main():
    cola = ColaDeReproduccion()
    ruta_directorio = sys.argv[1] if len(sys.argv) > 1 else "."
    if not os.path.isdir(ruta_directorio):
        print("Ruta no válida: " + ruta_directorio)
        sys.exit(-1)
    agregar_canciones(cola, ruta_directorio)
    reproductor = Reproductor(cola)
    ventana_reproductor = VentanaReproductor(reproductor)
    ventana_reproductor.actualizar()

    pyglet.app.run()
    sys.exit(0)

if __name__ == '__main__':
    main()
