# Ejercicio 5

pila = []

print("Prioridades:")
print("1 = Alta")
print("2 = Media")
print("3 = Baja")

cantidad = int(input("Ingrese la cantidad de interrupciones: "))

prioridades = {
    1: "Alta",
    2: "Media",
    3: "Baja"
}

actual_nombre = ""
actual_prioridad = 99

for i in range(cantidad):
    nombre = input(f"\nIngrese el nombre de la interrupción {i+1}: ")
    prioridad = int(input("Ingrese la prioridad: "))

    # Si no hay interrupción en proceso, se atiende directamente
    if actual_nombre == "":
        actual_nombre = nombre
        actual_prioridad = prioridad
        print("Atendiendo:", actual_nombre, "- Prioridad", prioridades.get(actual_prioridad, "Desconocida"))

    # Si llega una de mayor prioridad, interrumpe a la actual
    elif prioridad < actual_prioridad:
        pila.append([actual_nombre, actual_prioridad])
        print("Se guarda en pila:", actual_nombre, "- Prioridad", prioridades.get(actual_prioridad, "Desconocida"))

        actual_nombre = nombre
        actual_prioridad = prioridad
        print("Atendiendo ahora:", actual_nombre, "- Prioridad", prioridades.get(actual_prioridad, "Desconocida"))

    # Si no tiene mayor prioridad, queda pendiente
    else:
        pila.append([nombre, prioridad])
        print("Queda pendiente:", nombre, "- Prioridad", prioridades.get(prioridad, "Desconocida"))

print("\nFinaliza la interrupción actual:", actual_nombre)

print("\nRetomando interrupciones guardadas:")
while len(pila) > 0:
    inter = pila.pop()
    print("Retomando:", inter[0], "- Prioridad", prioridades.get(inter[1], "Desconocida"))