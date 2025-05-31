#45.Implementar un sistema de notas para estudiantes.
notas_estudiantes = {}

def agregar_notas():
    nombre = input("Escribe el nombre del estudiante: ")
    notas = []
    print("Ingresa las notas del estudiante (escribe 'fin' para terminar):")
    while True:
        entrada = input("Nota: ")
        if entrada.lower() == "fin":
            break
        try:
            nota = float(entrada)
            if 0 <= nota <= 10:
                notas.append(nota)
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Por favor, ingresa un número válido o 'fin' para terminar.")
    notas_estudiantes[nombre] = notas
    print(f"Notas de {nombre} guardadas.")

def mostrar_notas():
    if not notas_estudiantes:
        print("No hay notas registradas.")
        return
    for nombre, notas in notas_estudiantes.items():
        promedio = sum(notas) / len(notas) if notas else 0
        print(f"{nombre}: Notas = {notas}, Promedio = {promedio:.2f}")

def sistema_notas():
    while True:
        print("\nOpciones:")
        print("1. Agregar notas de un estudiante")
        print("2. Mostrar todas las notas y promedios")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            agregar_notas()
        elif opcion == "2":
            mostrar_notas()
        elif opcion == "3":
            print("Saliendo del sistema de notas.")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

sistema_notas()


















