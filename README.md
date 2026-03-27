# TAREA13M1_CETCIS

En estos ejercicios se utilizó la estructura de datos pila basada en el principio LIFO (Last In, First Out), donde el último elemento en entrar es el primero en salir.  

Las soluciones se implementaron de forma simple usando listas y operaciones básicas como:
- append() → insertar (push)
- pop() → eliminar (pop)

---

## Ejercicio 1
Se utilizó una pila para almacenar los movimientos del robot.  
Cuando se encuentra un obstáculo, los movimientos se desapilan para deshacer la ruta en orden inverso.  

---

## Ejercicio 2
Se implementó una pila para verificar si los símbolos `()`, `{}`, `[]` están correctamente balanceados.  
Los símbolos de apertura se apilan y los de cierre los desapilan verificando coincidencia.  

---

## Ejercicio 3
Se simuló la encapsulación de datos en redes, las capas se agregan a la pila antes de enviar el mensaje y se eliminan en orden inverso al recibirlo.  
Esto representa el funcionamiento de protocolos como TCP/IP.

---

## Ejercicio 4
Se utilizó una pila para controlar el orden de dibujo de superficies.  
Las superficies se ordenan por distancia y luego se apilan para que al desapilar se dibujen desde las más lejanas hasta las más cercanas, simulando la oclusión.

---

## Ejercicio 5
Se simuló el manejo de interrupciones anidadas usando una pila.  
Cuando llega una interrupción de mayor prioridad, la actual se guarda en la pila.  
Luego, se retoman las interrupciones en orden inverso.  
