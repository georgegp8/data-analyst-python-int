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

