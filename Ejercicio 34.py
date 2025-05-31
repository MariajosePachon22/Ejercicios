#34.Comprobar si dos palabras son anagramas.
palabra1 = "roma"
palabra2 = "amor"
lista1 = list(palabra1)
lista2 = list(palabra2)
lista1.sort()
lista2.sort()
if lista1 == lista2:
    print("Son anagramas.")
else:
    print("No son anagramas.")











