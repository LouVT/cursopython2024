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

