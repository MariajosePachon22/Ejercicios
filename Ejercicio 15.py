#15.Calcular la suma de los primeros N números naturales.
N = int(input("Ingresa un número natural N: "))
if N < 1:
    print("Por favor ingresa un número natural mayor que 0.")
else:
    suma = N * (N + 1) // 2
    print(f"La suma de los primeros {N} números naturales es: {suma}")


