#27.Contar la frecuencia de cada letra en una cadena.
texto = input("Escribe una palabra: ")
frecuencias = {}
for letra in texto:
    if letra in frecuencias:
        frecuencias[letra] += 1
    else:
        frecuencias[letra] = 1
print("Frecuencia de letras:")
for letra in frecuencias:
    print(letra, ":", frecuencias[letra])







