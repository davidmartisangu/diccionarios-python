base_datos1 = [("Juan", "juan@example.com", "555-1234"), ("Maria",
"maria@example.com", "555-5678"), ("Pedro", "pedro@example.com", "555-9012")]

base_datos2 = [("Juan", "Calle 123", ["Libro1", "Libro2"]), ("Maria", "Calle 456", ["Libro3"]),
("Luis", "Calle 789", ["Libro4"])]

#CLIENTES QUE APARECEN EN AMBAS BASES DE DATOS
nombres_base_datos1=set([tupla[0] for tupla in base_datos1]) #obtenemos los nombres de la base de datos 1
nombres_base_datos2=set([tupla[0] for tupla in base_datos2]) #obtenemos los nombres de la base de datos 2

nombres_comunes=nombres_base_datos1 & nombres_base_datos2  #intersección lo mismo que nombres_base_datos1.interseccion(nombres_base_datos2)
print(tuple(nombres_comunes)) #nos la piden en forma de tupla

#BASE DE DATOS CON LOS CLIENTES COMUNES Y CON LOS DATOS DE LAS DOS BASES
base_datos_comunes=[]
for i in base_datos1:
    if i[0] in nombres_comunes:
        for j in base_datos2:
            if j[0] ==i[0]:
                datos_comunes=i+j[1:]
                base_datos_comunes.append(datos_comunes)
                break
print(base_datos_comunes)