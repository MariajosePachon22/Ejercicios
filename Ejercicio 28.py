#27.Contar la frecuencia de cada letra en una cadena.
entrada = input("Ingresa números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]
mayor = max(numeros)
segundo_mayor = None
#28.Encontrar el segundo número más grande en una lista.
for num in numeros:
    if num != mayor:
        if segundo_mayor is None or num > segundo_mayor:
            segundo_mayor = num
print("El segundo número más grande es:", segundo_mayor)







