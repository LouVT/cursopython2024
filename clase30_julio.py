#_____________________Conjuntos / set_______________________________
"""
conjunto = {1,2,3,4,5}
otro_conjunto = {"hola","como","estas","?"}
conjungto_vacio = set()"""

#son heterogeneos
"""variable1 = "esto es una variable"
datos = {1,-5,123.57,"una cadena","otros string",variable1}
print(datos)"""

#Puede incluir numeros, variables, strings, o tuplas.
#Pero no pude incluir objetos mutables como listas, diccionarios e incluso otros conjuntos.

"""conjunto24 = {{1,2},[1,2,3,4,6], 2}
print(conjunto24)""" #Debe dar error

"""lista= ({1,2,3,4,5})
print(lista)
print(set({1,1,2,2,2,3,3,4,4}))"""

#Funciones Integradas en SET/CONJUNTOS

#_Add_
"""numeros= {1,2,3,4}
numeros.add(5*5)
print(numeros)"""

#_Update_
numeros= {1,2,3,4}
numeros.update([5,6,4,7,8])
print(numeros)

#_Len_
print(len(numeros))

#_Discard_
numeros.discard(2)
print(numeros)

#_Remove_
#Remove y Discard funcionan de igual manera, a diferencia que en Discard si el elemento pasado como argumento no existe, lo ingnora. En cambio con Remove nos devolverá un error.

#_IN_
print(2 in numeros) #Devuelve False porque con Discard removimos el 2

#_Clear_
"numeros.clear()"

#_POP_
"""numeros1 = [1,2,3,4,5,6]
while numeros1:
    print("Se esta borrando:", numeros1.pop())"""

#______________________________Diccionario / Dict______________________________

colores = {"amarillo": "yellow", "azul": "blue", "rojo": "reed"}

print(colores["amarillo"])

colores["amarillo"] = "white"
print(colores) #Cambiamos el contenido, reemplazamos Yellow por White

edades = {"Juan": 26, "Esteban": 35, "Maria": 29}
edades["Juan"] +=5
edades["Maria"] *=2
print(edades)

#_Add_
numeros3 = {"uno": 1, "dos" :2, "tres" :3, "cuatro" : 4}
numeros3["cinco"] = 5
print(numeros3)

#_Update_
numeros3.update({"seis":6})
print(numeros3) 

#_Len_
print(len(numeros3)) 

#_Del_
del numeros3["dos"]
print(numeros3)

#_IN_
"dos" in numeros3
print("dos" in numeros3)

#_Clear_
"numeros3.clear()"

#_POP_
print(numeros3.pop("uno"))

#_________________PARTE 2 CLASE_____________________---

#__UPPER__
cadena = "Hola chicos"
print(cadena.upper())
#Devuelve lo escrito en Mayúscula

"""print("Hola como estan".upper())""" #Funciona de igual manera que el ej de arriba

#__LOWER__
string = "HOLA CHICOS"
print(string.lower())
#Devuelve al contrario de Upper, convierte lo escrio en minuscula

#__CAPITALIZE__
cadena1 = "hola amigos"
print(cadena.capitalize())
#Este devuelve el primer caracter en mayuscula

#__TITLE__
cadena2 = "hOLa mUNDO"
print(cadena.title())
#Devuelve la primera letra de cada palabra en mayuscula

#__COUNT__
cadena3 = "hOLa mUNDO esta cadena tiene muchas a"
print(cadena3.count("a"))
#Cuenta la cantidad del item que pongas

#__FIND__
cadena4 = "hOLa mUNDO esta cadena tiene muchas a"
print(cadena4.find("esta"))
#Devuelve el INDICE en el que se encuentra el item

#__RFIND__
cadena5 = "Hola amigo como estas amigo"
print(cadena5.rfind("amigo"))
#Es como el Find pero encuentra el que esté como ultimo

#__SPLIT__
cadena6 = "hOla MunDo"
print(cadena6.split())
#Devuelve lo escrito como una lista, separando por comas

#__JOIN__
cadena7= "Hola mundo"
print(",".join(cadena7))
#Separa por letra con lo que elijas

#__STRIP__
cadena8= "------------------Hola mundo----------------"
print(cadena8.strip("-"))
#Borra el item que desees

#__REPLACE__
cadena9= "Moron"
print(cadena9.replace("o","0"))
#Reemplaza el caracter por otro deseado

#____________________METODOS PARA LISTAS______________________

#__CLEAR__
letras = ["a","b","c","d","e","f"]
print(letras)
print(letras.clear())
#Borra todos los elementos de a lista

#__Extend__
numeros = [1,2,3,4,5]
numeros + [6,7,8,9,10]

lista1 = [1,2,3,4,5]
lista2 = [6,7,8,9]

lista1.extend(lista2)
print(lista1)

#__INSERT__
lista3 = [1,2,3,4,5,6]
lista3.insert(0,0)
print(lista3)
#Inserta un item en el indice que quiera

#__REVERSE__
lista4 =[1,2,3,4,5,6]
lista4.reverse()
print(lista4)
#Hace que lo escrito se devuelva al reves, arrancando por la derecha y termina a la izq.
#No se puede utilizar REVERSE en los string

#__SORT__
lista5 = [5,-10,35,0,-75,150]
lista5.sort()
print(lista5)
#Ordena una lista por menor

#__________________CONJUNTOS________________-
#__COPY__
"""set1 = {1,2,3,4}
set2 = set1.copy()
print(set2)"""
#Copia lo que tenga la el otro set

#__ISDISJOINT__
"""set3 = {1,2,3}
set4 = {3,4,5}
print(set3.isdisjoint(set2))"""
#Comprueba si los set son iguales

#__ISSUBSET__
"""set5 = {-1,99}
set6= {1,2,3,4,5}
print(set5.issubset(set6))"""
#Comprueba si el set es subset de otro set, comprueba si TODOS los items estan en el otro

#ISSUPERSET
"""set7= {1,2,3}
set8= {1,2}
print(set7.issuperset(set8))"""
#Comprueba si el set contiene algun numero que esté dentro del otro set

#__UNION__
"""set9= {1,2,3}
set10= {3,4,5}
set11 = set9.union(set10)
print(set11)"""
#Une un set con otro y te devuelve el resultado con un set nuevo

#__DIFERENCE__

set1 = {1,2,3}
set2 = {3,4,5}
print(set1.difference(set2))
#Encuentra las diferencias entre un set y el otro

#__DIFFERENCE_UPDATE__
"""set1 = {1,2,3}
set2 = {3,4,5}
set1.difference_update(set2)
print(set1)"""
#Guarda las diferencias de items en el set original, lo que le asigna de valor los items diferentes.

#__INTERSECTION__
"""set1 = {1,2,3}
set2 = {3,4,5}
set1.intersection(set2)"""
"""print(set1.intersection(set2))"""
#Devuelve la interseccion, osea el item en comun entre  los set

#__INTERSECTION_UPDATE__
set1 = {1,2,3}
set2 = {3,4,5}
set1.intersection_update(set2)
print(set1)
#Le asigna el nuevo valor al set con el item en comun

#_________________DICCIONARIOS__________________
#__GET__
"""colores = {"amarillo": "yellow", "azul": "blue", "rojo": "red"}
print(colores.get("verde", "no hay clave verde"))"""
#Busca un elemento atraves de su clave, en el caso de no encotrarlo va a devolver un valor por defecto que le indiquemos nosotros.

#__KEY__
"""colores = {"amarillo": "yellow","azul": "blue", "rojo": "red"}
print(colores.keys())"""
#Sirve para mostrar todas las claves de un diccionario, por si no lo recuerdas

#__VALUES__
"""colores = {"amarillo": "yellow", "azul": "blue", "rojo": "red"}
print(colores.values())"""
#Sirve para traer todos los valores del diccionario

#__ITEMS__
colores = {"amarillo": "yellow", "azul": "blue", "rojo": "red"}
print(colores.items())

#Crea una lista con clave y valor de un diccionario

for clave, valor in colores.items():
    print(clave,valor)
    
