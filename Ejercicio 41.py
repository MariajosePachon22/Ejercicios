#41.Encontrar el número que falta en una secuencia del 1 al N.
numeros = [1, 2, 4, 5, 6]  
N = 6
suma_total = N * (N + 1) // 2
suma_lista = 0
for num in numeros:
    suma_lista += num
faltante = suma_total - suma_lista
print("El número que falta es:", faltante)














