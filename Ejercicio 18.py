#18.Contar cuántos números pares e impares hay en una lista.
entrada = input("Ingresa números enteros separados por comas: ")
numeros = [int(x) for x in entrada.split(",")]
pares = 0
impares = 0
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print("Cantidad de números pares:", pares)
print("Cantidad de números impares:", impares)




