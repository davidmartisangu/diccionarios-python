'''Una red social tiene una base de datos de usuarios y sus correspondientes amistades.
Crea un programa que tome una base de datos de una red social como una lista de
tuplas, donde cada tupla contiene el nombre del usuario y una lista de sus amigos. Los
nombres repetidos en la lista de amigos corresponden a usuarios con varias cuentas
diferentes. Deberas eliminar las cuentas duplicadas y después devolver una tupla de
tuplas que contiene el número real de amigos por usuario y el usuario con más amigos.'''
red_social = [("Juan", ["Maria", "Pedro", "Luis"]), ("Maria", ["Juan", "Pedro","Juan"]), ("Pedro", ["Juan", "Maria"]), ("Luis", ["Juan"])]
list_red_social=[]
#--ELIMINAR LAS CUENTAS DUPLICADAS
for usuario,amigo in red_social: #recorro los usuarios y amigos
    amigos_unique=list(set(amigo))  #creo un set eliminando los amigos repetidos y los guardo en una lista
    list_red_social.append((usuario,amigos_unique)) #lo voy guardando en una lista de listas
print(tuple(list_red_social))

#--NÚMERO REAL DE AMIGOS POR USUARIO
lista_numero_amigos=[]
lista_usuarios=[]
for usuario,amigo in list_red_social:
    lista_usuarios.append(usuario)              # tambien lo podría haber sacadado con: lista_usua=[tupla[0] for tupla in red_social]
    lista_numero_amigos.append(len(amigo))

print(lista_numero_amigos)
print(lista_usuarios)
posicion_max_amigos=lista_numero_amigos.index(max(lista_numero_amigos))
print(f"El usuario con más amigos es {lista_usuarios[posicion_max_amigos]}")


