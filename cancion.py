from tinytag import TinyTag


class Cancion:
    """ Objeto que almacena informacion de una cancion: su ruta, titulo y artista.
    Obtiene la informacion a partir de los tags del archivo, si los tiene."""

    def __init__(self, ruta, titulo='Cancion desconocida', artista='Autor desconocido'):
        # Usar TinyTag para obtener la informacion de la cancion, sobreescribir con lo pasado por 
        # parametro solo si la informacion no se encuentra disponible
        self.ruta = ruta
        tag = TinyTag.get(ruta)
        get_titulo = tag.title
        get_artista = tag.artist
        if get_titulo:
            self.titulo = tag.title
        else:
            self.titulo = titulo
        if get_artista:
            self.artista = tag.artist
        else:
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
        """Devuelve True si la ruta de las canciones son iguales y False en caso contrario."""
        return self.ruta == otro.ruta

    def __str__(self):
        """Devuelve una cadena con una representación de la cancion."""
        return self.titulo

    def __repr__(self):
        """Devuelve una cadena con una representación de la cancion."""
        return self.titulo
