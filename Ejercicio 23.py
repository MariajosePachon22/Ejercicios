#23.Calcular la suma de los números pares hasta N
N = int(input("Ingresa un número: "))
suma = 0
for i in range(2, N + 1, 2):
    suma += i
print("La suma de los números pares hasta", N, "es:", suma)







