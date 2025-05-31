#33.Encontrar el número que más se repite en una lista.
numeros = [4, 2, 4, 6, 4, 2, 8, 6, 6]
mas_repetido = None
mayor_cantidad = 0
for numero in numeros:
    cantidad = 0
    for n in numeros:
        if n == numero:
            cantidad += 1
    if cantidad > mayor_cantidad:
        mayor_cantidad = cantidad
        mas_repetido = numero
print("El número que más se repite es:", mas_repetido)
print("Se repite", mayor_cantidad, "veces.")










