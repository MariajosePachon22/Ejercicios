#36.Imprimir un patrón de pirámide con asteriscos (*).
filas = 5
for i in range(1, filas + 1):
    espacios = filas - i
    estrellas = 2 * i - 1
    print(" " * espacios, end="")
    print("*" * estrellas)












