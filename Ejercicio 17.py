#17.Calcular el promedio de una lista de números.
entrada = input("Ingresa números separados por comas: ")
numeros = [float(x) for x in entrada.split(",")]
promedio = sum(numeros) / len(numeros)
print("El promedio es:", promedio)



