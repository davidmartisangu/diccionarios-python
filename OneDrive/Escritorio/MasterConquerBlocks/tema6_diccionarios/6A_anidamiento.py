#22. Crea un diccionario llamado "productos" que contenga dos entradas. Cada entrada representa un producto y tiene a su vez las claves "nombre" y "precio" con sus respectivos valores.
#Recorre el diccionario e imprime el nombre y precio de cada producto.
productos={
    "producto_1":{
        "nombre":"pollo",
        "precio":10,
    },
    "producto_2":{
        "nombre":"agua",
        "precio":1,
    }
}
for products,info in productos.items():
    print("\nProducto:",products)
    nombre_product=info["nombre"].title()
    precio_product=info["precio"]
    print("\tNombre producto:", nombre_product)
    print("\tPrecio producto:", precio_product)
#23. Agrega un nuevo producto al diccionario "productos" utilizando una nueva clave y valor. Imprime el diccionario actualizado.
producto_3={"nombre":"leche","precio":1.70}
productos["producto_3"]=producto_3
print(productos)
#24.Crea un diccionario llamado "equipos" que contenga tres entradas. Cada entrada representa un equipo deportivo y tiene las claves "nombre" y "jugadores" con sus
#respectivos valores. Los valores de "jugadores" deben ser listas con los nombres de los jugadores. Recorre el diccionario e imprime el nombre del equipo y la lista de jugadores.
equipos={
    "equipo_1":{
        "nombre":"valenciacf",
        "jugadores": ["vicente","pablo","edu"],
    },
    "equipo_2": {
        "nombre":"realmadrid",
        "jugadores":["raul","casillas","ronaldo"],
    },
    "equipo_3":{
        "nombre":"barcafc",
        "jugadores":["puyol","pique","messi"],
    },
}
for teams,info in equipos.items():
    print("Equipo: ", info["nombre"].title(),"\nJugadores: ",info["jugadores"])
    print("")

#25.Agrega un nuevo equipo al diccionario "equipos" utilizando una nueva clave y valor. La lista de jugadores debe contener al menos tres nombres. Imprime el diccionario actualizado.
equipo_4={"nombre":"sevilla","jugadores":["joaquin","mark","tomas"]}
equipos["equipo_4"]=equipo_4
print(equipos)

#26.Actualiza la lista de jugadores de uno de los equipos existentes en el diccionario "equipos". Agrega un nuevo jugador a la lista. Imprime el diccionario actualizado.
equipos["equipo_1"]["jugadores"].append("aimar")
print("\n",equipos)