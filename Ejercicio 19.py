#19.Ordenar una lista de números de menor a mayor.
entrada = input("Ingresa números separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]
numeros.sort()
print("Lista ordenada de menor a mayor:", numeros)





