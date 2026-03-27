# Ejercicio 4

cantidad = int(input("Ingrese la cantidad de superficies: "))

superficies = []

# Ingreso de datos
for i in range(cantidad):
    nombre = input(f"Nombre de la superficie {i+1}: ")
    distancia = float(input(f"Distancia de {nombre}: "))
    superficies.append([nombre, distancia])

# Ordenar de más lejana a más cercana
superficies.sort(key=lambda x: x[1], reverse=True)

# Pasar a la pila
pila = []

print("\nAgregando superficies a la pila...")
for s in superficies:
    pila.append(s)
    print("Se agregó:", s[0], "- Distancia:", s[1])

print("\nOrden de renderizado:")

# Dibujar usando la pila
while len(pila) > 0:
    superficie = pila.pop()
    print("Dibujando:", superficie[0], "- Distancia:", superficie[1])