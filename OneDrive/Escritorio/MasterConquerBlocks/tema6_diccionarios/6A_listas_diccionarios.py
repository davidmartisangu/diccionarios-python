#18.Crea una lista llamada "estudiantes" que contenga dos diccionarios. Cada diccionario representa a un estudiante y tiene las claves "nombre" y "edad" con sus respectivos valores.
#Recorre la lista e imprime el nombre y edad de cada estudiante.
usuario_1={
    "Nombre":"David",
    "Edad":35,
}
usuario_2={
    "Nombre":"Vicen",
    "Edad":40,
}
estudiantes=[usuario_1,usuario_2]
print(estudiantes)
for usuarios in estudiantes:
    for nombre,edad in usuarios.items():
        print(nombre,edad)
        
#19.Agrega un nuevo estudiante a la lista "estudiantes" utilizando un diccionario con las mismas claves "nombre" y "edad". Imprime la lista actualizada.
usuario_3={
    "Nombre":"Ainhoa",
    "Edad":12,
}
estudiantes.append(usuario_3)
print(estudiantes)
#20.Elimina el segundo estudiante de la lista "estudiantes". Imprime la lista actualizada.
del estudiantes[1]  #estudiantes.remove(usuario_2)
print(estudiantes)
#21.Actualiza la edad del primer estudiante en la lista "estudiantes" a un nuevo valor. Imprime la lista actualizada.
usuario_1["Edad"]=36    #estudiantes[0]["Edad"] =36
print(estudiantes)