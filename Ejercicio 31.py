#31.Contar cuántas veces aparece un número en una lista.
numeros = [1, 3, 5, 3, 7, 3, 8, 5]
numero_a_contar = 3
contador = 0
for numero in numeros:
    if numero == numero_a_contar:
        contador += 1
print("El número", numero_a_contar, "aparece", contador, "veces.")







