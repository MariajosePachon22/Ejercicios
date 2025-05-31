#12.Sumar los dígitos de un número.
numero = int(input("Ingresa un número entero: "))
numero = abs(numero)
suma = 0
for digito in str(numero):
    suma += int(digito)
print("La suma de los dígitos es:", suma)

