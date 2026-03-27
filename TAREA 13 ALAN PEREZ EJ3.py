# Ejercicio 3

mensaje = input("Ingrese el mensaje a enviar: ")

pila = []

print("\nEncapsulando mensaje...")

pila.append("Aplicación")
print("Capa agregada:", "Aplicación")

pila.append("Transporte")
print("Capa agregada:", "Transporte")

pila.append("Red")
print("Capa agregada:", "Red")

pila.append("Enlace")
print("Capa agregada:", "Enlace")

print("\nMensaje enviado con capas.")
print("Contenido de la pila:", pila)

print("\nRecibiendo paquete. Desencapsulando...")

while len(pila) > 0:
    capa = pila.pop()
    print("Se quitó la capa:", capa)

print("\nMensaje recibido:", mensaje)