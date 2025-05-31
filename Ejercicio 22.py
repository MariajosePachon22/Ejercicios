#22.Generar un número aleatorio entre 1 y 100.
import random
def generar_numero_aleatorio():
    numero = random.randint(1, 100)#El modulo random y a la funcion randint devuelve un numero entre los que estan en el parentesis  
    return numero
def main():
    numero_aleatorio = generar_numero_aleatorio()
    print("Número aleatorio generado:", numero_aleatorio)
main()







