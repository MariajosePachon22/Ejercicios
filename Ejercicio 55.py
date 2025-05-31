#55.Obtener el último dígito de un número.
numero = input("Ingresa un número: ")
if numero.startswith('-'):
    numero = numero[1:]
ultimo_digito = numero[-1]
print("El último dígito es:", ultimo_digito)


















