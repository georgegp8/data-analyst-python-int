# ================================================
# Lógica, Flujo de Control y Filtrado
# Ejercicios: Operadores de Comparación
# ================================================

# ------------------------------------------------
# Sección 1: Igualdad
# ------------------------------------------------
# Para comprobar si dos valores de Python, o variables, son iguales puedes utilizar ==.
# Para comprobar la desigualdad, necesitas !=.
# Para refrescar la memoria, echa un vistazo a los siguientes ejemplos que dan
# como resultado True. No dudes en probarlos.
#
#   2 == (1 + 1)
#   "intermediate" != "python"
#   True != False
#   "Python" != "python"
#
# Cuando escribas estas comparaciones en un guión, tendrás que envolverlas con
# una función print() para ver el resultado.

# Instrucciones:
# - Escribe código para ver si True es igual a False.
# - Escribe código Python para comprobar si -5 * 15 no es igual a 75.
# - Pregunta a Python si las cadenas "pyscript" y "PyScript" son iguales.
# - ¿Qué ocurre si comparas booleanos y enteros? Escribe código para ver si True y 1 son iguales.

# Comparison of booleans
print(True == False)

# Comparison of integers
print(-5 * 15 != 75)

# Comparison of strings
print('pyscript' == 'PyScript')

# Compare a boolean with an integer
print(True == 1)

# ------------------------------------------------
# Sección 2: Mayor y menor que
# ------------------------------------------------
# En el vídeo, Hugo también habló de los signos menor que y mayor que, < y > en Python.
# Puedes combinarlos con un signo igual: <= y >=.
# Presta atención: <= es una sintaxis válida, pero =< no lo es.
#
# Todas las expresiones Python del siguiente fragmento de código se evalúan como True:
#
#   3 < 4
#   3 <= 4
#   "alpha" <= "beta"
#
# Recuerda que, para comparar cadenas, Python determina la relación según el orden alfabético.

# Instrucciones:
# - Escribe expresiones Python, envueltas en una función print(), para comprobar si:
#   - x es mayor o igual que -10. Ya se ha definido x.
#   - "test" es menor o igual que y. Ya se ha definido y.
#   - True es mayor que False.

# Comparison of integers
x = -3 * 6
print(x >= -10)

# Comparison of strings
y = "test"
print('test' <= y)

# Comparison of booleans
print(True > False)

# ------------------------------------------------
# Sección 3: Comparar matrices
# ------------------------------------------------
# También puedes utilizar operadores de comparación con matrices NumPy.
#
# ¿Recuerdas areas, la lista de medidas de superficie de las distintas habitaciones
# de la casa de Introducción a Python? Esta vez hay dos matrices NumPy: my_house y
# your_house. Ambas contienen las zonas de la cocina, el salón, el dormitorio y el
# cuarto de baño en el mismo orden, para que puedas compararlos.

# Instrucciones:
# - Utilizando operadores de comparación, genera matrices booleanas que respondan
#   a las siguientes preguntas:
#   - ¿Qué zonas de my_house son mayores o iguales que 18?
#   - También puedes comparar dos matrices NumPy elemento a elemento.
#     ¿Qué zonas de my_house son más pequeñas que las de your_house?
#   - ¡Asegúrate de envolver ambos comandos en una declaración print() para que
#     puedas inspeccionar la salida!

# Create arrays
import numpy as np
my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than or equal to 18
print(my_house >= 18)

# my_house less than your_house
print(my_house < your_house)

