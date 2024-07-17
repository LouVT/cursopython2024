#____________Clase 16 de Julio, 2da parte de la clase 2 de Julio______

"""edad = int(iput("Qué edad tenes?"))
"if edad >= 18:"
    "print("Sos adulto")"""
    
"""If False:
    "print("Imprimime laconcición verdadera")"""""
    
"""a = 2
b = 10"""
"""if a == 2:
    print("a vale", a)
    if b == 10:
        print("a y b vale: , b")
        """
        
"""  if a == 2 and b == 10:
        print("a vale", a,"y b vale", b) """
        

#Else

"""numero = 24
if numero >=36:
    print("El numero es mayor o igual a 36")
else:
    print("El numero es menor a 36")
"""

#Elise sino, si

"""numero = 15
if numero >=18:
    print("Es un adulto")
elif numero == 17:  
    print("Casi es mayor")
else:
    print("Es menor")"""
    
"""dato_entrada = input("ESCRIBI ENTRAR, SALUDO O SALIR:").upper()
if dato_entrada == "ENTRAR":
    print("Bienvenido")
elif dato_entrada == "SALUDO":
    print("Hola, como estas?")
elif dato_entrada == "SALIR":
    print("Te estás yendo")
else:
    print("No reconozco la interacción")"""
    
#".upper()" sirve para que python reconozca por igual el dato ingresado, ya sea que esté en Mayúscula o Minúscula.

"""nota = int(input("Escribi tu nota:")) #Input sirve para que el usuario pueda escribir
if nota >= 9:
    print("Sobresaliente")
elif nota >=7:
    print("Muy bien")
elif nota >=6:
    print("Bien")
elif nota >=4:
    ("Regular") 
else:
    print("Desaprobaste")   """
    
#___Se puede utilizar de dos formas, son progtamas equivalentes
    
"""nota = int(input("Escribi tu nota:"))
if nota >= 9:
    print("Sobresaliente")
if nota >=7 and nota <9:
    print("Muy bien")
if nota >=6 and nota <7:
    print("Bien")
if nota >=4 and nota <6:
    ("Regular") 
else:
    print("Desaprobaste")   """

#Sentencias Iterativas
#WHILE
#FOR

#El flujo de ejecución de una sentencia WHILE:
#1.Evalua la condición devolviendo FALSE O TRUE
#2.S si la condición es FALSE, se sale sentencia WHILE y continua la ejecución con la siguiente sentencia.
#3.Si la condición es TRUE, ejecuta cada una de las sentencia que hay en el bloque del código y regresa al paso 1.

"""numero = 10
while numero >0:
    print(numero)
    numero-= 1
print("Terminó el conteo")"""
    
"""n = 0
while n <=5:
    n+=1
    print("N vale", n)"""
    
#while condición:
#   introducciones de while 
#else
#   si no se terminó con break
#   intrucciones de while-else

"""chance = 1
while chance <=3:
    txt = input("Escribe SI:")
    if txt == "SI":
        print("OK, lo conseguiste en el intento", chance)
        break
    chance +=1
else:
    print("Has agotado tus tres intentos")"""
    
#Break es un comando para romper un flujo, corta hasta ahi la ejución para pasar a lo siguiente.

#_____BREAK - CONTINUE - PASS____

#BREAK CIERRA EL BUCLE CON UNA CONDICIÓN EXTERNA
"""n = 5
while n < 10:
    n-=1
    if n == 2:
        print("ahora n vale 2 y salimos del bucle")
        break
    print("n vale", n)"""
    
#CONTINUE SIRVE PARA OMITIR UNA PARTE DEL BUCLE EN LA CUAL SE ACTIVA UNA CONDICIÓN EXTERNA.

"""m = 0 
while m < 10:
    m+=1
    if m==2:
        print("Coninuamos con la siguiennte iteración")
        continue
    print("m vale", m)"""
    
#PASS sirve para manejar la condición sin que el bucle se vea afectado de ninguna manera.

"""l = 0
while l < 10:
    l+=1
    if l ==2:
        pass
    print("l vale", l)"""
    

#FOR 

"""lista = [1,2,3,4,5]

for valor in lista:
    print("Soy un item de la lista y valgo", valor)"""


#FOR = PARA
#Valor es simplemente una variable creada del objeto que se esta iterando.
#IN = en
#lista es la lista, tupla, etc... que va a ser íterada

"""lista_1  = [0,1,2,3,4,5,6,7,8,9,10]
for num in lista_1:
    print("soy el valor de la lista_1 y valgo", num)
    num*=5
    print("Soy un valor de la lista_1 y ahora valgo", num)"""
    
"""indice = 0
numeros= [0,1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    numeros[indice] *=5
    indice +=1
    #tambien se puede con indice = numero
print(numeros)

texto = "Hola mundo, estoy usando for en python"
for letra in texto:
    print(letra)
    
texto2 = ""
for letra in texto:
    texto2= letra*2
print(texto2)"""
    
    
