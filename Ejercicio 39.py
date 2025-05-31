#39.Implementar un generador de contraseñas.
import random
letras = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
simbolos = "!@#$%^&*"
todos = letras + numeros + simbolos
longitud = int(input("¿De cuántos caracteres quieres tu contraseña? "))
contraseña = ""
for i in range(longitud):
    caracter_aleatorio = random.choice(todos)
    contraseña += caracter_aleatorio
print("Tu contraseña es:", contraseña)













