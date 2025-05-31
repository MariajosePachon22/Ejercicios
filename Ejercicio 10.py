#10.Invertir un número entero.
numero = int(input("Ingresa un número entero: "))
if numero < 0:
    invertido = int("-" + str(abs(numero))[::-1])
else:
    invertido = int(str(numero)[::-1])
print("Número invertido:", invertido)

