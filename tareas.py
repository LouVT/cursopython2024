#DESTINADO A LAS TAREAS

#_______________________________________________________________-

#CLASE 25/6: TENIENDO DOS LISTA LA CUAL LLAMAREMOS lista_1 y lista_2 hay que hacer los siguientes ejercicios

#Añadir a la lista_1 el entero 4567 y despues el string "UNAHUR"

#Añadir a la lista_2 el string "EDUCACION" y despues el entero 789

#Crear una lista_3 con todos los elementos de la lista_1 MENOS el último

#Crear una lista_4 con todos los elementos de la lista_2 MENOS el primero y último

#Crear una lista_5 con todos los elementos de la lista_3 y de la lista_4


#                              AHORA CON TUPLAS
#Crear una variable llamada tupla con más de 15 items y printear lo siguiente:

# El ultimo item de la tupla creada, el numero de items de la misma, la posicion donde se encuentra algun item que haya dentro, una lista con los ultimos cuatro items de la tupla, un item que haya en la posicion 8, el numero de veces que se repite algún item dentro de la misma.


string_unahur= "UNAHUR"
lista_1 = [4567, string_unahur ]
print(lista_1)

string_educación = "EDUCACIÓN"
lista_2 = ["EDUCACIÓN", 789]
print(lista_2)

lista_3 = [4567, string_unahur]
lista_3.pop()
print(lista_3)

lista_4 = [string_educación, 789]
lista_4.pop(0)
lista_4.pop()
print(lista_4)

lista_5 = [lista_3, lista_4]
print(lista_5)

tupla = (12,32,-21,333,1,75,23,99,405,44,10,403,11,74,22)
print(tupla[-1]) #Ultimo item
print(len(tupla)) #Números de items
print(tupla.index(75)) #Posicion de algun item
print(tupla[-4:]) #Los ultimos 4
print(tupla[8]) #Numero en posicion 8
print(tupla.count(11))

#____________________CLASE 30 DE JULIO_______________________


#SETS
#Es una variable grupo:
#Añadir a las sguiente personas: Jose, Maria, Gerardo, Fabian.
#Eliminar a las personas: Fernando, Federico, Francisco.

grupo = {"Fernando", "Federico", "Francisco", "Ricardo"}

grupo.update(["Jose","Maria", "Gerardo", "Fabian"])
grupo.discard("Fernando")
grupo.discard("Federico")
grupo.discard("Francisco")
print(grupo)

#DICCIONARIOS
animalitos = {"elefante":""}
#Añadir al diccionario las claves perro, gato y tucan con sus valores "Tobi", "Michi", y "Diego"

#Modificar la clave elefante por delfin
animalitos.update({"Perro": "Tobi", "Gato": "Michi", "Tucan": "Diego"})

print(animalitos)

