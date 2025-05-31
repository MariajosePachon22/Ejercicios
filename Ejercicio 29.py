#29.Rotar una lista a la derecha una posición.
entrada = input("Ingresa números separados por comas: ")
lista = [int(x) for x in entrada.split(",")]
ultimo = lista[-1]
for i in range(len(lista) - 1, 0, -1):
    lista[i] = lista[i - 1]
lista[0] = ultimo
print("Lista rotada a la derecha una posición:", lista)








