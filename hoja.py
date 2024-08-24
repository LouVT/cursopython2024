def cadena_mayusculas(lista_cadenas):
    lista_mayusculas = [cadena.upper() for cadena in lista_cadenas]
    return lista_mayusculas

lista_original = ["perro", "maria", "ojala", "volver"]
lista_mayusculas = cadena_mayusculas(lista_original)

print(lista_mayusculas) 