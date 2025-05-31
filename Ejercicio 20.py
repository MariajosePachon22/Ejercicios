#20.Verificar si una palabra es un palíndromo.
palabra = input("Ingresa una palabra: ")
palabra_limpia = palabra.lower().replace(" ", "")
if palabra_limpia == palabra_limpia[::-1]:
    print("Es un palíndromo.")
else:
    print("No es un palíndromo.")






