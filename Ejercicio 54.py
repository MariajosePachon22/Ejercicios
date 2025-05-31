#54.btener el primer dígito de un número.
numero = input("Ingresa un número: ")
if numero.startswith('-'):
    numero = numero[1:]
primer_digito = numero[0]
print("El primer dígito es:", primer_digito)

















