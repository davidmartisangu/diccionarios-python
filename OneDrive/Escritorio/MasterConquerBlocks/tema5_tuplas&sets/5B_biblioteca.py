lista_libros = [("El aleph", 'Borges'), ('Cien años de soledad', 'Márquez'), ('La ciudad y los perros', 'Llosa')]
lista_nombres=["Manuel","Juan","Mario"]
lista_apellidos=[]
lista_titulos=[]
for titulo,autor in lista_libros:#recorro la lista y obtengo una lista de autores y de titulos
    lista_apellidos.append(autor)
    lista_titulos.append(titulo)
#print(lista_apellidos)
lista_nombre_completo=[]
for i in range(len(lista_apellidos)):#añado los nombres a la lista de apellidos
    nombre=lista_nombres[i]+" "+lista_apellidos[i]
    lista_nombre_completo.append(nombre)
print(lista_nombre_completo)

lista_tuplas=tuple(zip(lista_titulos,lista_nombre_completo))#uno las dos listas creando una tupla
print(lista_tuplas)