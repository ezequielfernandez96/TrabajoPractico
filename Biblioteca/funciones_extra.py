from biblioteca import Biblioteca

class BibliotecaExtendida(Biblioteca):
    def __init__(self):
        super().__init__()

    def buscar_libro_por_autor(self, autor):
        """
        Busca y retorna todos los libros escritos por un autor específico.
        """
        libros_autor = []
        for libro in self.libros:
            if libro['autor'] == autor:
                libros_autor.append(libro)
        return libros_autor if libros_autor else None

    def filtrar_libros_por_palabra(self, palabra):
        """
        Filtra y retorna libros cuyo título contenga la palabra especificada.
        """
        libros_filtrados = []
        for libro in self.libros:
            if palabra.lower() in libro['titulo'].lower():
                libros_filtrados.append(libro)
        return libros_filtrados if libros_filtrados else None

    def actualizar_autor_libro(self, titulo, nuevo_autor):
        """
        Actualiza el autor de un libro dado su título.
        Retorna True si el libro fue encontrado y el autor actualizado, False si no se encontró el libro.
        """
        for libro in self.libros:
            if libro['titulo'] == titulo:
                libro['autor'] = nuevo_autor
                return True
        return False
