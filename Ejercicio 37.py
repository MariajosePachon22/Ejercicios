#37.Verificar si una cadena es un pangrama (contiene todas las letras del abecedario).
frase = input("Escribe una frase: ")
frase = frase.lower()
abecedario = "abcdefghijklmnopqrstuvwxyz"
es_pangrama = True
for letra in abecedario:
    if letra not in frase:
        es_pangrama = False
        break
if es_pangrama:
    print("Es un pangrama")
else:
    print("No es un pangrama")












