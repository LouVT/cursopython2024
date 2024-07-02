#___________________Operadores_______________

# Operando [operador] Operando
#          + / * -  
# Operadores aritméticos (+,-,*,/)
# Expresiones aritméticas: 2+2, 5-1, -1.9 * 100, 28/3
# Expresiones algebráicas: radio + 3.14 (nota1 + nota2)/2

# Tipo lógicos: BOOLEANO o binario
# Es el tipo de dato más básico de la información racional y representa VERDADERO y FALSO

# __NEGACIÓN__
# No verdadero = Falso (FALSE)
# No falso = Verdadero (TRUE)

#__OPERADORES RELACIONALES__
#Los operadores racionales son simbolos que se usan para comparar dos valores. Si el resultado de la comparacion es correcto la expresión va a ser considerada TRUE, de lo contrario será FALSE

"print(1+1 == 3)" 

#__IGUALDAD__
# El operador de igualdad sirve para preguntarle al programa si ambos son iguales.
# Nos va a devolver TRUE si son iguales, y FALSE si son distintos
# Este operador se escribe con dos signos igual (==)

a = 3 
print(a == 3) 

#__DESIGUALDAD O DISTINTO__
# El operador DISTINTO sirve para preguntarle a nuestro programa si ambos operados son distintos.
# Va a devolver TRUE si son distintos, y FALSE si son iguales
# Este operador se escribe con un signo de exclamación y un signo de igual (!=)

print(a != 3)

#__MENOR QUE__
# El operador MENOR QUE sirve para preguntarle a nuestro programa si el primer operando es menor que el segundo operandon
# Nos va devolver TRUE si el primero es menor al segundo y FALSE si el primero es mayor al segundo.
# 7 < 3
print(7<3)

#__MENOR IGUAL QUE__
# El operador MENOR IGUAL QUE sirve para preguntarle a nuestro programa si el primer operando es menor que el segundo operando o si ambos son iguales.
# Nos va a devolver TRUE si el primero es menor o igual al segundo, y FALSE si el primero es mayor que el segundo.
# Este opreador se escribe con un signo menor que y un igual (<=)
print(7<=3)
print(10<=10)

#__MAYOR QUE__
# El operador MAYOR QUE sirve para preguntarle a nuestro programa si el primer operando es mayor que el segundo operando.
# Nos va a devolver TRUE si el primero es mayor que el segundo y FALSE si el primero es menor que el seundo.
# Este operador se escribe con un signo de mayor (>)
print(7>6)
print(1>2)

#__MAYOR IGUAL QUE__
# El operador MAYOR IGUAL QUE sirve para preguntarle a nuestro programa si el primer operando es mayor que el segundo operando o si ambos son iguales.
# Nos va a devolver TRUE si el primero es mayor o igual que el segundo y FALSE si el primero es menor que el seundo.
# Este operador se escribe con un signo de mayor y un igual (>=)
print(7>=3)
print(10>=10)

# Podemos hacer operaciones relacionales en strings inclusive.

print("Hola" == "Hola")

b = "Hola"

print(b[1]== "o") # Acá le estoy pidiendo al programa si el indice 1 de la variable b es igual a "o"

print(False == True)
print(10>= 2*4)
print(33/3 ==11)
print(True > False) #True tiene un valor aritmetico de 1 y False un valor de 0, por lo tanto TRUE es mayor a FALSE.
print(True*5 == 2.5*2)

#___________________OPERADORES LÓGICOS___________________
#NOT
#NOT es la negación, o tambien conocido como NO. Solo afecta a los tipos lógicos TRUE y FALSE, y solo requiere un operando en una expresión.
print(not True)
print(not True == False)

#__CONJUCIÓN Y DISYUNCIÓN__
#Conjución viene de conjunto, agrupa uniendo.
#Disyunción viene de disyunto, agrupa separando.

#____AND____
#Es conocido como Y
#Va a unir una o varias setntencias lógicas
#Verdadero y verdadero

print(2>1 and 5>2)
print(5>25 and 20>1)

#True AND True = True
#True AND False = False 
#False AND False = False
#False AND True = False

#___OR___
#Es O en ingles.
#Es DISTUNCIÓN (separa)
#Si le pregunta a Python por dos afirmaciones  al menos una es TRUE, python me va a decir que la afirmación es TRUE.

print(2>1 or 5>2)
print(5<20 or 20<1)

#True OR True= True
#True OR False= True
#False OR True= True
#False OR False= False


#__Ejercicios mental de Expresiones__

#Not False : True
#Not 3 == 5 : True
#33/3 == 11 and 5>2 : True
#True Or False : True
#True*5 = 2.5*2 or 123>= 23 : True
#12>7 and True<False : False

#______________NORMAS DE PRECEDENCIA_______________
#1. TÉRMINOS ENTRE PARENTESIS
#2. POTENCIACIÓN Y RAÍCES
#3. MULTIPLICACIÓN Y DIVISIÓN
#4. SUMA Y RESTA

d = 15
e = 12
print(d**e / 3 **e / e*d >= and not(d%e **2) != 0)