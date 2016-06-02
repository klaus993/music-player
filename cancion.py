from tinytag import TinyTag, TinyTagException


class Cancion:
    """ Objeto que almacena informacion de una cancion: su ruta, titulo y artista.
    Obtiene la informacion a partir de los tags del archivo, si los tiene."""

    def __init__(self, ruta, titulo="Cancion desconocida", artista="Autor desconocido"):
        # Usar TinyTag para obtener la informacion de la cancion, sobreescribir con lo pasado por 
        # parametro solo si la informacion no se encuentra disponible
        self.ruta = ruta
        try:
            tag = TinyTag.get(ruta)
            self.titulo = tag.title
            self.artista = tag.artist
        except (TinyTagException, LookupError, OSError) as e:
            print("Error: " + str(e))
            self.titulo = titulo
            self.artista = artista

    def obtener_ruta(self):
        """ Devuelve la ruta del archivo de la cancion."""
        return self.ruta

    def obtener_titulo(self):
        """ Devuelve el titulo de la cancion."""
        return self.titulo

    def obtener_artista(self):
        """ Devuelve el artista de la cancion."""
        return self.artista

    def __eq__(self, otro):
        return self.ruta==otro.ruta
        
    def __str__(self):
        return self.titulo