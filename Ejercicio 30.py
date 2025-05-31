#30.Implementar una calculadora simple con +, −, *, /.
num1 = int(input("Ingresa el primer número: "))
operacion = input("Ingresa la operación (+, -, *, /): ")
num2 = int(input("Ingresa el segundo número: "))
if operacion == "+":
    resultado = num1 + num2
elif operacion == "-":
    resultado = num1 - num2
elif operacion == "*":
    resultado = num1 * num2
elif operacion == "/":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: división entre cero"
else:
    resultado = "Operación no válida"
print("Resultado:", resultado)









