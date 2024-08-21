"""import clase6_agosto
clase6_agosto. saludar()

sirve para traer las funciones de otros apartados

from clase6_agosto import saludar
saludar()"""
"""
from collections import Counter 
b = [1,2,3,5,1,2,3,9,7,2]
print(Counter(b))
print(Counter("palabrutas"))

from collections import defaultdict
d = defaultdict(str) #tipo cadena por defecto
print(d["cosa"])
print(d)

from collections import OrderedDict
m = OrderedDict()
m=["uno"]= "one"
m=["dos"]= "two"
m=["tres"]= "three"
print(m)
"""
"""from datetime import datetime
dt= datetime.now() #fecha y hora actual

print(dt)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)

print("{}:{}:{}". format(dt.hour, dt.minute, dt.second))
print("{}/{}/{}". format(dt.day, dt.month,dt.year))

import random

#flotante aleatorio >= 0 y< 1.0
print(random.random(1,10))

#Flotante aleatorio >=1 y <10.0
print(random.uniform(1,10))

#Entero aleatorio de 0 a 19, 20 excluido
print(random.randrange(20))

#Entero aleatorio de 0 a 1000
print(random.randrange(0,1001))

#Enero aleatorio de 0 a 1000 cada 2 numeros, multiples de 5
print(random.randrange(0,1001,2))"""

#_________

while (True):
    try:
        n= float (input("Introduce un número:"))
        m= 4
        print(n,"/", n, "=", n/m) 
        break
    except:
        print("ocurrio un error, introduci un nro")
    else:
        print("todo sucedio corractamente")
        break
