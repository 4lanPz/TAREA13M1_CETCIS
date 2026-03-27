# Ejercicio 2

codigo = input("Ingrese una expresión o código: ")

pila = []
balanceado = True
tiene_simbolos = False

for caracter in codigo:
    if caracter in "({[":
        pila.append(caracter)
        tiene_simbolos = True

    elif caracter in ")}]":
        tiene_simbolos = True

        if len(pila) == 0:
            balanceado = False
            break

        ultimo = pila.pop()

        if caracter == ")" and ultimo != "(":
            balanceado = False
            break
        elif caracter == "}" and ultimo != "{":
            balanceado = False
            break
        elif caracter == "]" and ultimo != "[":
            balanceado = False
            break

if len(pila) != 0:
    balanceado = False

print("\nResultado:")

if not tiene_simbolos:
    print("No se encontraron símbolos para validar.")
elif balanceado:
    print("La sintaxis está balanceada correctamente.")
else:
    print("La sintaxis NO está balanceada.")