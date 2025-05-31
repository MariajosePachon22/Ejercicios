#44.Implementar un sistema de reservas de boletos de cine.
asientos = [False] * 10  # 
def mostrar_asientos():
    print("Estado de los asientos:")
    for i, ocupado in enumerate(asientos, start=1):
        estado = "Ocupado" if ocupado else "Libre"
        print(f"Asiento {i}: {estado}")

def reservar_asiento():
    mostrar_asientos()
    try:
        asiento = int(input("Elige un asiento del 1 al 10 para reservar: "))
        if asiento < 1 or asiento > 10:
            print("Número de asiento inválido.")
            return
        if asientos[asiento - 1]:
            print("Lo siento, ese asiento ya está reservado.")
        else:
            asientos[asiento - 1] = True
            print(f"Asiento {asiento} reservado con éxito.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def sistema_reservas():
    while True:
        print("\nOpciones:")
        print("1. Mostrar asientos")
        print("2. Reservar asiento")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_asientos()
        elif opcion == "2":
            reservar_asiento()
        elif opcion == "3":
            print("Gracias por usar el sistema de reservas.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

sistema_reservas()

asientos = [False] * 10  

def mostrar_asientos():
    print("Estado de los asientos:")
    for i, ocupado in enumerate(asientos, start=1):
        estado = "Ocupado" if ocupado else "Libre"
        print(f"Asiento {i}: {estado}")

def reservar_asiento():
    mostrar_asientos()
    try:
        asiento = int(input("Elige un asiento del 1 al 10 para reservar: "))
        if asiento < 1 or asiento > 10:
            print("Número de asiento inválido.")
            return
        if asientos[asiento - 1]:
            print("Lo siento, ese asiento ya está reservado.")
        else:
            asientos[asiento - 1] = True
            print(f"Asiento {asiento} reservado con éxito.")
    except ValueError:
        print("Por favor, ingresa un número válido.")

def sistema_reservas():
    while True:
        print("\nOpciones:")
        print("1. Mostrar asientos")
        print("2. Reservar asiento")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            mostrar_asientos()
        elif opcion == "2":
            reservar_asiento()
        elif opcion == "3":
            print("Gracias por usar el sistema de reservas.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")
sistema_reservas()

















