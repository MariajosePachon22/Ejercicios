#53.Contar el número de dígitos en un número.
numero = input("Ingresa un número: ")
if numero.startswith('-'):
    numero = numero[1:] 
cantidad_digitos = len(numero)
print("El número tiene", cantidad_digitos, "dígitos.")
















