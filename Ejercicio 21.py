#21.Convertir un número decimal a binario.
numero = int(input("Ingresa un número decimal entero: "))
if numero < 0:
    print("Por favor ingresa un número entero no negativo.")
else:
    if numero == 0:
        binario = "0"
    else:
        binario = ""
        n = numero
        while n > 0:
            residuo = n % 2
            binario = str(residuo) + binario
            n = n // 2

    print(f"El número {numero} en binario es: {binario}")







