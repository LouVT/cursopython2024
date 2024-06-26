#____________Clase Martes 25 de Junio_____________

#Longitud de String
#Función LEN

"""esto_es_un_string = "Hola soy un string"

print(len(esto_es_un_string))

string1 = "       "  #cuenta la cantidad de un espacio ya sea un vacio

print(len(string1))"""

#Rebanar un string
#Función SLICING [inicio:fin:paso]
#Inicio va a ser el indice del primer caracter de la cadena que queremos rebanar.
#Fin va a ser el indice del último caracter no incluido de la cadena que queremos rebanar.
#Paso: Indica cada cuantos caracteres vamos a selecciones entre las posiciones de inicio y fin.

"""saludo = "Hola, cómo estan?"
saludo[0:3:1]
print(len(saludo))
print(saludo[0:3:1])
print(saludo[0:3:2])
print(saludo[0:17:2])

palabra = "Pithon"
print(palabra)

print(palabra[1])

palabra = palabra[0:1] +"y"+ palabra[2:]

print(palabra)"""

#____________________LISTA Y TUPLAS__________________

"""mi_lista = [-11,20,3,41]
print(mi_lista)

otra_lista = ["hola","como","estas","?"]

variable_1 = "una variable"

listita = [1,-10,123.5,"un string","otro string",variable_1]

print(listita)

print(listita[0])
print(listita[-1])

print(listita[-2:])

print(listita + [otra_lista, "algo random"])"""

"""números =[1,2,3,4,5,6,7,8,9,10]
print(números+[11,12,13,14,15,16])

números = [0,2,4,5,10,15,20]
números[3] = 8
print(números)

letras = ["a","b","c","d","e","f"]
letras[:3] = ["A","B","C"]
print(letras)

letras = ["a","b","c","d","e","f"]
letras[:3] = [] #Lista vacia "[]"
print(letras)
#Pasar una lista vacia es como "borrar" la parte seleccionada.

equipos = ["Morón","River","Boca","Independiente"]
print(equipos)
equipos = []
print(equipos)"""

#___________________________FUNCIÓN APPEND____________________

#Nos permite agregar un nuevo item al final de una lista - se escribe mi_lista.appeend(item_a_agregar)
números = [1,2,3,4,5,6]
números.append(7)
print(números)

#Tambien podemos utilizar la función LEN acá - LEN se escribe len(la_lista_a_consultar_su_longitud)
print(len(números))

equipos = ["Morón","River","Boca","Independiente"]
print(equipos)
print(len(equipos))

#FUNCIÓN POP
#La función POP es todo lo contrario a Append, porque va a eliminar el último item de una lista - pop.()

"""equipos = ["Morón","River","Boca","Independiente"]
equipos.pop()
print(equipos)"""
#Si ingreso dentro del parentesis una posición segun indice, pop eliminará el indice correspondiente
equipos = ["Morón","River","Boca","Independiente"]
equipos.pop(2)
print(equipos)

#__________________________FUNCIÓN COUNT__________________________

#La función COUNT cuenta el número de veces que nuestro item se repetite en una lista - se escribre la_lista_a_contar.count(el_item_que_quieren_que_cuente)
numeros_varios = [1,2,3,4,5,9,12,55,20,20,20,3,4,59]
#En este caso el item 20, se repite 3 veces
print(numeros_varios.count(20))

#___________________________INDEX________________________

#Busca el item y nos devuelve en que indice está - se escribe la_lista.index(lo_que_queremos_buscar)

numeros_varios = [1,2,3,5,9,12,55,20,20,20,3,4,59]
print(numeros_varios.index(59))

#__________________TUPLAS___________________

#Las tuplas son similares a las listas, la GRAN diferencia es que las tuplas son IMPUTABLES.
#Se declaran con parentesis - mi_tupla(1,2,3,4)

mi_tupla = (1,2,3,4,5)
print(mi_tupla)

otra_tupla = (1,5,-100,"cadena","otra cadena/string",mi_tupla)

print(otra_tupla)

print(otra_tupla[0])

print(otra_tupla[2:])

print(len(otra_tupla))

print(otra_tupla.index(5))

print(otra_tupla.count(1))

otra_tupla,append(100)