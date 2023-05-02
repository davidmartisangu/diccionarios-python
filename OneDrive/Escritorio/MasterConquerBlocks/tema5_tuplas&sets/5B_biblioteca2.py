#--input data
lista_libros = [("El aleph", 'Jose Luis Borges'), ('Cien años de soledad', 'Grabril Garcia Márquez'), ('La ciudad y los perros', 'Jose Maria Llosa')]
nombres=[tupla[1] for tupla in lista_libros]
titulos=[tupla[0] for tupla in lista_libros]


lista_apellidos=[]
'''for i in nombres:
    apellido=i.split()
    surname=apellido[-1]
    lista_apellidos.append(surname)
print(lista_apellidos)
tupla_lista_libros=tuple(zip(titulos,lista_apellidos))
print(tupla_lista_libros)'''

for titulo,autor in lista_libros:
    apellido=autor.split()[-1]
    lista_apellidos.append((titulo,apellido))
print(lista_apellidos)
