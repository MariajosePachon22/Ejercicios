#52.Determinar todos los primos para N números.
N = int(input("Ingresa un número: "))
print("Números primos hasta", N, ":")
for num in range(2, N + 1):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        print(num)


















