#__________________RESULTADO EJ 1________________

"""Ejercicio 1: Números y Cadenas de Caracteres
Escribe un programa que pida al usuario dos números enteros y realice lo siguiente:
Muestra la suma de los dos números.
Muestra el producto de los dos números.
Muestra la concatenación de los dos números (como texto)."""

primer_numero = int(input("Escriba un número entero:"))
segundo_numero = int(input("Escriba otro número entero:"))

print(primer_numero+segundo_numero)
print(primer_numero*segundo_numero)

print(str(primer_numero)+str(segundo_numero))


"""
Pide al usuario una cadena de texto. Luego muestra:
La cadena en mayúsculas.
La longitud de la cadena.
La cadena invertida.
La cantidad de veces que aparece una letra específica (elige una letra y pídesela al usuario)."""

cadena_del_usuario = input("Escriba algun texto:")

print(cadena_del_usuario.upper())
print(len(cadena_del_usuario))
print(cadena_del_usuario[::-1])

elegir_letra = input("Escribe algun texto que contenga muchas 'A':")
print(elegir_letra.count("a"))

                            

""" Escribe un programa que convierta un número decimal a binario y viceversa. """

def decimal_a_binario(decimal):
    if decimal <= 0:
        return "0"
    binario = ""
    while decimal > 0:
        residuo = decimal % 2
        decimal = decimal // 2
        binario = str(residuo) + binario
    return binario


numero_decimal = int(input("Ingresa un número decimal: "))
numero_binario = decimal_a_binario(numero_decimal)
print(f"El número {numero_decimal} en binario es {numero_binario}")

def binario_a_decimal(binario):
    decimal = 0
    longitud = len(binario)
    
    for i in range(longitud):
        digito = int(binario[i])
        decimal += digito * (2 ** (longitud - i - 1)) 
    return decimal


binario = input("Introduce un número binario: ")
decimal = binario_a_decimal(binario)
print(f"El número decimal es: {decimal}")


""" Pide al usuario una cadena y un número entero. Muestra la cadena repetida el número de veces indicado por el número entero."""

otra_cadena = input("Escribe un texto:")
numero_a_repetir = int(input("Inserta un número entero: "))

print(otra_cadena*numero_a_repetir) 

#__________________RESULTADO EJ 2________________

""" Crea una lista con los nombres de tres frutas. Luego:
Añade dos frutas más a la lista.
Ordena la lista alfabéticamente.
Muestra la lista completa.
Elimina una fruta de la lista y muestra el resultado. """

lista_frutas = ["frutilla", "kiwi", "durazno"]
print(lista_frutas)

lista_frutas.append("naranja")
lista_frutas.append("uva")
print(lista_frutas)

lista_frutas.sort()
print(lista_frutas)

lista_frutas.pop(3)
print(lista_frutas)

"""  Crea una tupla con los nombres de dos ciudades. Luego:
Muestra el primer y último elemento de la tupla.
Convierte la tupla en una lista, añade una nueva ciudad y muestra la lista resultante.
  """
  
tupla_ciudades = ("Buenos Aires","Neuquen")
print(tupla_ciudades[0])
print(tupla_ciudades[-1])

lista_ciudades = list(tupla_ciudades)
lista_ciudades.append("Salta")
print(lista_ciudades)

""" Crea una lista de números enteros y muestra:
El número mayor de la lista.
El número menor de la lista.
El promedio de los números en la lista. """

lista_numeros = [1,23,32,-4,65,43,2,87]
numero_mayor= max(lista_numeros)
print(numero_mayor)

numero_menor= min(lista_numeros)
print(numero_menor)

suma_de_lista = sum(lista_numeros)
print(round(suma_de_lista/8))

""" Escribe un programa que reciba una lista de cadenas y muestre la lista con todas las cadenas en mayúsculas."""
    
def cadena_mayusculas(lista_cadenas):
    lista_mayusculas = [cadena.upper() for cadena in lista_cadenas]
    return lista_mayusculas

lista_original = ["perro", "maria", "ojala", "volver"]
lista_mayusculas = cadena_mayusculas(lista_original)

print(lista_mayusculas) 
 
    
#__________________RESULTADO EJ3________________

""" Escribe un programa que pida un número al usuario. Muestra si el número es par o impar. """     

numero = int(input("Inserte un número:"))

if numero %2 == 0:
        print("Es un numero par") 
else:
        print("Es un numero impar")

""" Crea un programa que simule un menú simple con las siguientes opciones:
Saludar
Despedirse
Salir
Dependiendo de la opción elegida, muestra un mensaje correspondiente. Si se elige 3, el programa debe terminar. """

menu = input("Seleccionar SALUDAR, DESPEDIRSE O SALIR:").upper()
if menu == "SALUDAR":
    print("Buenos dias, todo bien?")
elif menu == "DESPEDIRSE":
    print("Nos vemos")
elif menu == "SALIR":
    print("Te fuiste")
else:
    print("Error, intente de nuevo.")
    
"""Escribe un programa que pida un número al usuario y determine si es positivo, negativo o cero."""

numero2 = int(input("Inserte un número:"))

if numero2 > 0:
    print("Es un numero positivo") 
elif numero2 < 0:
    print("Es un numero negativo")
elif numero2 == 0:
    print("Es cero")
    
""" Escribe un programa que muestre los números del 1 al 10 utilizando un bucle .for """

numeros_hasta10 = [1,2,3,4,5,6,7,8,9,10]
for num in numeros_hasta10:
    print(num)
    num +=1
    
""" Escribe un programa que calcule la suma de los números del 1 al 100 utilizando un bucle .while """

numero4= 1
while numero4 <101:
    print(numero4)
    numero4 +=1 
    

#__________________RESULTADO EJ4________________

""" Crea dos conjuntos con algunos números. Luego:
Muestra la unión de los dos conjuntos.
Muestra la diferencia entre los dos conjuntos.
Muestra los elementos comunes en ambos conjuntos. """

conjunto1 = {1,2,3,4,5,6}
conjunto2 = {3,5,7,8,9,10}    

conjunto3= conjunto1.union(conjunto2)
print(conjunto3)

print(conjunto1.difference(conjunto2))
print(conjunto2.difference(conjunto1))

print(conjunto1.intersection(conjunto2))

""" Crea un diccionario con tres nombres como claves y edades como valores. Luego:
Muestra la edad del primer nombre en el diccionario.
Añade un nuevo nombre y edad al diccionario.
Elimina un nombre del diccionario y muestra el resultado.
Muestra todas las claves y todos los valores del diccionario. """

diccionario = {"Luis": "20", "Robert": "44", "Juli": "11"}
print(diccionario.get("Luis"))

diccionario.update({"Nino":6})
print(diccionario)

del diccionario ["Juli"]
print(diccionario)

print(diccionario.keys())
print(diccionario.values())

""" Crea un diccionario con los nombres de cinco productos como claves y sus precios como valores. Luego:
Muestra el precio de un producto específico.
Incrementa el precio de todos los productos en un 10%.
Muestra el diccionario actualizado. """

productos = {"Lavandina": 1400, "Azucar": 2000, "Shampoo": 1500, "Levadura": 500, "Sarten": 9.990}

print(productos.get("Levadura"))

productos["Lavandina"] *= 1.1
productos["Azucar"]*= 1.1
productos["Shampoo"] *= 1.1
productos["Levadura"]*= 1.1
productos["Sarten"]*= 1.1

print(productos)


""" Crea un conjunto con los números del 1 al 5 y otro conjunto con los números del 4 al 8. Muestra:
La intersección de los dos conjuntos.
La diferencia simétrica entre los dos conjuntos. """

conjunto4 = {1,2,3,4,5}
conjunto5 = {4,5,6,7,8}
print(conjunto4.intersection(conjunto5))

print(conjunto4.symmetric_difference(conjunto5))

#__________________RESULTADO EJ5________________

""" Define una función que reciba un nombre y muestre un saludo. Luego llama a esta función con tu propio nombre.saludar(nombre)"""

def saludar(nombre):
     saludar2 = print("Hola {} ¿Todo bien?".format(nombre))
     return saludar2


saludar("Lourdes")

""" Define una función que reciba dos números y retorne su suma. Luego prueba la función con dos números diferentes.suma(a, b) """

def suma(numero1, numero2):
    return numero1 + numero2

suma_de_numeros1 = suma (10,6)
print(suma_de_numeros1)
    
suma_de_numeros2 = suma (5,12)
print(suma_de_numeros2)

""" Define una función que reciba una edad y retorne si la edad es mayor o igual a 18 y en caso contrario. Prueba la función con diferentes edades.es_mayor_de_edad(edad)TrueFalse """

def es_mayor_de_edad(edad):
    return edad >= 18

print(es_mayor_de_edad(18))
print(es_mayor_de_edad(80))    
print(es_mayor_de_edad(5))