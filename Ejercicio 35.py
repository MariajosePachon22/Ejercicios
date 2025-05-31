#35.Encontrar el índice de la primera ocurrencia de un elemento en una lista.
numeros = [5, 3, 7, 3, 9, 1]
buscar = 3
indice = 0
for numero in numeros:
    if numero == buscar:
        print("El número", buscar, "se encuentra en el índice", indice)
        break  
    indice += 1











