#43.Generar números primos hasta un valor dado.
maximo = int(input("Generar números primos hasta: "))
primos = []
for num in range(2, maximo + 1):
    es_primo = True
    for i in range(2, num):
        if num % i == 0:
            es_primo = False
            break
    if es_primo:
        primos.append(num)
print("Números primos hasta", maximo, "son:", primos)

















