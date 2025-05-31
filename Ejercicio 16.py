#16.Encontrar el mínimo y máximo en una lista de números.
entrada = input("Ingresa números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]
minimo = min(numeros)
maximo = max(numeros)
print("El número mínimo es:", minimo)
print("El número máximo es:", maximo)


