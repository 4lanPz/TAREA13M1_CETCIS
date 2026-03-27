# Ejercicio 1:

pila = []

print("Movimientos:")
print("1 = Avanzar")
print("2 = Girar Derecha")
print("3 = Girar Izquierda")

cantidad = int(input("Ingrese la cantidad de movimientos: "))

# Guardar movimientos
for i in range(cantidad):
    mov = int(input(f"Ingrese el movimiento {i+1}: "))
    pila.append(mov)

# nombres de movimientos
nombres = {
    1: "Avanzar",
    2: "Girar Derecha",
    3: "Girar Izquierda"
}

# Mostrar ruta
print("\nRuta guardada:")
for mov in pila:
    print(nombres.get(mov, "Desconocido"), end=" -> ")

print("\n\nObstáculo encontrado. Deshaciendo ruta...")

# Deshacer movimientos
while len(pila) > 0:
    mov = pila.pop()

    if mov == 1:
        print("Deshacer: Retroceder")
    elif mov == 2:
        print("Deshacer: Girar Izquierda")
    elif mov == 3:
        print("Deshacer: Girar Derecha")
    else:
        print("Movimiento inválido")