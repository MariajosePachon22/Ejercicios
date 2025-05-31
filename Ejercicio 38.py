#38.Crear una función que invierta una lista sin usar .reverse().
def invertir_lista(lista_original):
    lista_invertida = []
    i = len(lista_original) - 1
    while i >= 0:
        lista_invertida.append(lista_original[i])
        i -= 1
    return lista_invertida
mi_lista = [10, 20, 30, 40, 50]
lista_resultado = invertir_lista(mi_lista)
print("Lista original:", mi_lista)
print("Lista invertida:", lista_resultado)












