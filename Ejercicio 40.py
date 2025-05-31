#40.Comprimir una cadena eliminando caracteres repetidos consecutivos.
cadena = "aaabbccdddeee"
cadena_comprimida = ""
for i in range(len(cadena)):
    if i == 0 or cadena[i] != cadena[i-1]:
        cadena_comprimida += cadena[i]
print("Cadena original:", cadena)
print("Cadena comprimida:", cadena_comprimida)














