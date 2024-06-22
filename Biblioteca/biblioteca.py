class Biblioteca:
    def __init__(self):
        self.libros = []

    def agregar_libro(self, libro):
        self.libros.append(libro)

    def buscar_libro_por_titulo(self, titulo):
        for libro in self.libros:
            if libro['titulo'] == titulo:
                return libro
        return None

    def eliminar_libro(self, titulo):
        for libro in self.libros:
            if libro['titulo'] == titulo:
                self.libros.remove(libro)
                return True
        return False

    def listar_libros(self):
        return self.libros

    def contar_libros(self):
        return len(self.libros)

