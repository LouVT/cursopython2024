#DESTINADO A LAS TAREAS


#CLASE 18/6: CREAR UN SCRIPT EN EL QUE PODAMOS CALCULAR LA NOTA FINAL EN BASE A 5 EXAMENES, ESTOS EXAMENES EQUIVALEN A UN PORCENTAJE DE LA NOTA FINAL.

# LA NOTA NUMERO 1 CORRESPONDE AL 20% DE LA NOTA FINAL.
# LA NOTA NUMERO 2 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 3 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 4 CORRESPONDE AL 10% DE LA NOTA FINAL.
# LA NOTA NUMERO 5 CORRESPONDE AL 50% DE LA NOTA FINAL.

#A esto se lo suele llamar promedio ponderado: no todos los valores tienen el mismo "peso".
#Por ejemplo, dado el ejercicio de arriba me conviene sacarme una mejor nota en el examen donde la nota vale casi el 50% de la nota final.

primera_nota = 20

segunda_nota = 10

tercera_nota = 10

cuarta_nota = 10

quinta_nota = 50

nota_uno = input("Escribe tu nota del primer examen:")

nota_dos = input("Escribe tu nota del segundo examen:")

nota_tres = input("Escribe tu nota del tercer examen:")

nota_cuatro = input("Escribe tu nota del cuarto examen:")

nota_cinco = input("Escribe tu nota del quinto examen:")

print (nota_uno%20)


promedio_uno = print (nota_uno%20)

promedio_dos = print(nota_dos%10)

promedio_tres = print(nota_tres%10)

promedio_cuatro = print(nota_cuatro%10)

promedio_cinco = print(nota_cinco%50)

nota_final = print(promedio_uno+promedio_dos+promedio_tres+promedio_cuatro+promedio_cinco)

print(nota_final)








