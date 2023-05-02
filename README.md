# tuplas-sets
EJERCICIOS 5B

RED SOCIAL:
Una red social tiene una base de datos de usuarios y sus correspondientes amistades.
Crea un programa que tome una base de datos de una red social como una lista de
tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los
nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas
diferentes. Deberas eliminar las cuentas duplicadas y después devolver una tupla de
tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.
Pista 1: Tus datos de entrada podrían ser así —> red_social = [("Juan", ["Maria", "Pedro",
"Luis"]), ("Maria", ["Juan", “Pedro”,”Juan”]), ("Pedro", ["Juan", "Maria"]), ("Luis", [“Juan”])]
Pista 2: Para eliminar duplicidades puedes usar sets

LA BIBLIOTECA:
Una biblioteca tiene una lista de libros y sus autores. Crea un programa que tome la lista
de libros y sus autores como una lista de tuplas, donde cada tupla contiene el título del
libro y el nombre del autor, y devuelva una nueva lista de tuplas que contenga el título del
libro y el apellido del autor.
Pista: Tus datos de entrada podrían ser así —> lista_libros = [(‘El aleph', 'Borges'), ('Cien
años de soledad', 'Márquez'), ('La ciudad y los perros', 'Llosa')]

DATOS CLIENTES:
Una compañía tiene dos bases de datos de clientes. La primera base de datos contiene
el nombre del cliente, la dirección de correo electrónico y el número de teléfono. La
segunda base de datos contiene el nombre del cliente, la dirección y el historial de
pedidos. Escribe un programa que tome las dos bases de datos como listas de tuplas y
devuelva una nueva lista de tuplas que contenga solo los clientes que aparecen en
ambas bases de datos. Los clientes se consideran iguales si tienen el mismo nombre.
Pista: Tus datos de entrada podrían ser así —>
base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria",
"maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", “555-9012")]
base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]),
("Luis", "Calle 789", ["Libro4"])]
