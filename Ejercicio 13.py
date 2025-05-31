#13.Verificar si un número es primo.
numero = int(input("Ingresa un número entero: "))
if numero < 2:
    print("No es un número primo.")
else:
    es_primo = True
    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            es_primo = False
            break
    if es_primo:
        print("El número es primo.")
    else:
        print("El número no es primo.")


