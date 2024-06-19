"Clase martes 18 de junio" 

# Números

#Números con los que se maneja Python:

## Números enteros = INT O LONG
## Long 27361273817823L

## Número FLOAT  = Números con decimales
# EJ : 0.32
# -33.895

##COMPLEX
# 33.8j

## SUMA +
## RESTA - 
## MULTIPLICACIÓN *
## POTENCIA **
## DIVISIÓN (coeciente) /
## DIVISIÓN (parte enetera) //
## PROMEDIO %

## PROCEDENCIA DE LOS OPERADORES:
# 1- TERMINOS ENTRE PARENTESIS
# 2- POTENCIACIÓN Y RAICES
# 3- MULTIPLICACIÓN Y DIVISIÓN 
# 4- SUMA Y RESTA

""" print (15+8)

print (30-5)

print (80*2)

print (30.5-5)

print (25**5)

print (16/4)

print (16//4)

print (24%5) """

#_____________________ STRING = STR (CADENA DE TEXTO)___________________

#COMILLAS DOBLE: ""
#COMILLAS SIMPLES: ''
    
print ("hola, estamos en un curso de python")

print ("hola mundo")

#print = imprimir 

print ("un string \t con tabulador") 

print (" otro string pero con \n salto de linea")

#______________________VARIABLES__________________________

# LAS VARIABLES EN PYTHON SON COMO ETIQUETAS QUE NOS PERMITEN HACER REFERENCIAS A LOS DATOS.
# POR CDA DATO QUE APARECCE EN UN PROGRAMA, PYTHON VA A CREAR UN OBJETO QUE LO CONTIENE.
# CADA OBJETO VA A TENER:
#1- UN IDENTIFICADOR ÚNICO (id)
#2- UN TIPO DE DATO (entero, decimal, string, etc)
#3- UN VALOR(el propio dato dentro)
# LAS VARIABLES EN PYTHON NO GUARDAN LOS DATOS.

dni = 45496042

a = 2

print (a)

print (dni)

mi_variable = 1947

print (mi_variable)

# DEFINIR UNA VARIABLE: A=2

# LA VARIABLE NO PUEDE SER UN NÚMERO NEGATIVO
# EL NOMBRE DE UNA VARIABLE SIEMPRE DEBE EMPEZAR POR UNA LETRA O POR UN GUION BAJO (_) snake_case
# LOS NOMBRES EN LAS VARIABLES NO PUEDEN INCLUIR ESPACIOS EN BLANCO
# LOS NOMBRES DEBEN SER ESCRITOS EN MINÚSCULAS PARA MAYOR COMODIDAD Y FUNCIONAMIENTO

mi_fecha_de_nacimiento = "21 de marzo"

print (mi_fecha_de_nacimiento)

# METODO DE SALIDA = PRINT()

# METODO DE ENTRADA = INPUT()

""" nombre = input("hola escribi tu nombre:")

print (nombre) """

print (30+9)

# LA FUNCIÓN INPUT POR DEFECTO CONVIERTE LOS DATOS DE ENTRADAS EN UN STRING (ES UNA CADENA). AUNQUE LE ESTEMOS ESCRIBIENDO UN NÚMERO

a = 20
b = 30

resultado = a+b

print (resultado)

c = 100
d = 200

print (c+d)

# LOS DATOS DE ENTRADA SE PODRIAN CONVERTIR DE STR (STRING) 

e = 30
""" f = input ("cual es tu edad?") """ #ESTE ES UN EJ DE UN DATO DE ENTRADA QUE LO TOMA COMO CADENA DE TEXTO
""" f = int (input("cual es tu edad"))  """#CONVERSIÓN DE TIPO: DE ESTA FORMA LOGRAMOS QUE PYTHON CONVIERTA STR DE ENTRADA EN UN NÚMERO

""" print (e*f) """

cadena_de_texto = "python sos lo mejor de mi vida tkmmmmmmmmmmmmmmmmmmmmmmmmmmm yo"
anio_del_curso = "2024"

print(cadena_de_texto + anio_del_curso)

# A LA SUMA DE LOS STRINGS LO VAMOS A LLAMAR CONCATENACIÓN

# LOS INDICES VIENEN: 0(primer caracter), 1(segundo caracter), etc
# LOS INDICEES INVERSOS VIENEN: -1(último caracter), -2(penúltimo caracter),etc
#  P  Y  T  H  O  N
#  0  1  2  3  4  5 indices
# -6 -5 -4 -3 -2 -1 indice inverso

print (cadena_de_texto[-1])

