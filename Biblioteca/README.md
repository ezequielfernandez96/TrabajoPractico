Introducción:

En este proyecto, Pytest se utiliza para organizar y ejecutar pruebas que validan el funcionamiento correcto de los métodos implementados en la clase Biblioteca del archivo biblioteca.py. Este archivo define una clase llamada Biblioteca que proporciona métodos para gestionar una colección de libros. Está diseñada para ser una representación virtual de una biblioteca permitiendo operaciones como agregar, buscar, eliminar, listar y contar libros.

Se ha agregado un archivo test_biblioteca.py que dentro contiene funciones "test_" que basicamente al momento de ejecutar pytest las analiza y confirma si encuentra o no errores.

se ha agregado tambien un archivo funciones_extra.py que expande la funcionalidad de la clase Biblioteca, se ha creado una clase extendida llamada BibliotecaExtendida. Esta nueva clase puede agregar métodos adicionales que permitan operaciones más avanzadas con la colección de libros.

Análisis:

El framework Pytest se encarga de buscar errores dentro de la biblioteca. Proporciona resultados claros sobre el éxito o fallo de cada prueba, asegurando que la funcionalidad de la biblioteca virtual se mantenga robusta y precisa.

Ejemplo de Uso:

En la consola, ejecutar "Pytest" y comenzará a analizar todas las funciones de prueba que esten escritas de la siguiente manera: "test_"



