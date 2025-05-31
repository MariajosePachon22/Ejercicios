#9.Calcular el factorial de un número.
num = int(input("Ingresa un número entero no negativo: "))
if num < 0:
    print("El factorial no está definido para números negativos.")
else:
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    print(f"El factorial de {num} es: {factorial}")
