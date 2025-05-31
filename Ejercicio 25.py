#25.Hallar el MCM (Mínimo Común Múltiplo) de dos números.
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
mayor = max(a, b)
while True:
    if mayor % a == 0 and mayor % b == 0:
        mcm = mayor
        break
    mayor += 1
print("El MCM de", a, "y", b, "es:", mcm)







