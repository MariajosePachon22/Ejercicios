#24.Hallar el MCD (Máximo Común Divisor) de dos números.
a = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
mcd = 1
for i in range(1, min(a, b) + 1):
    if a % i == 0 and b % i == 0:
        mcd = i
print("El MCD de", a, "y", b, "es:", mcd)






