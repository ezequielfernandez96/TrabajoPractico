import pytest
from biblioteca import Biblioteca

@pytest.fixture
def biblioteca_ejemplo():
    biblioteca = Biblioteca()
    biblioteca.agregar_libro({'titulo': 'El Principito', 'autor': 'Antoine de Saint-Exupéry'})
    biblioteca.agregar_libro({'titulo': 'Don Quijote de la Mancha', 'autor': 'Miguel de Cervantes'})
    return biblioteca

def test_agregar_libro(biblioteca_ejemplo):
    assert biblioteca_ejemplo.contar_libros() == 2
    biblioteca_ejemplo.agregar_libro({'titulo': 'Cien años de soledad', 'autor': 'Gabriel García Márquez'})
    assert biblioteca_ejemplo.contar_libros() == 3

def test_buscar_libro_por_titulo(biblioteca_ejemplo):
    libro = biblioteca_ejemplo.buscar_libro_por_titulo('El Principito')
    assert libro is not None
    assert libro['autor'] == 'Antoine de Saint-Exupéry'

    assert biblioteca_ejemplo.buscar_libro_por_titulo('Libro Inexistente') is None

def test_eliminar_libro(biblioteca_ejemplo):
    assert biblioteca_ejemplo.eliminar_libro('Don Quijote de la Mancha') is True
    assert biblioteca_ejemplo.contar_libros() == 1
    assert biblioteca_ejemplo.eliminar_libro('Libro Inexistente') is False

def test_listar_libros(biblioteca_ejemplo):
    libros = biblioteca_ejemplo.listar_libros()
    assert len(libros) == 2
    assert {'titulo': 'El Principito', 'autor': 'Antoine de Saint-Exupéry'} in libros
    assert {'titulo': 'Don Quijote de la Mancha', 'autor': 'Miguel de Cervantes'} in libros

def test_contar_libros(biblioteca_ejemplo):
    assert biblioteca_ejemplo.contar_libros() == 2
    biblioteca_ejemplo.agregar_libro({'titulo': 'Rayuela', 'autor': 'Julio Cortázar'})
    assert biblioteca_ejemplo.contar_libros() == 3
