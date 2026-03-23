# ================================================
# Bucles
# Ejercicios: Estructuras de Datos - Parte 1
# ================================================

# ------------------------------------------------
# Sección 1: Bucle por un diccionario
# ------------------------------------------------
# En Python 3, necesitas el método items() para hacer un bucle por un diccionario:
#
#   world = { "afghanistan":30.55,
#             "albania":2.77,
#             "algeria":39.21 }
#
#   for key, value in world.items() :
#       print(key + " -- " + str(value))
#
# ¿Recuerdas el diccionario europe que contenía los nombres de algunos países europeos como clave
# y sus capitales como valor correspondiente? Adelante, escribe un bucle para iterar por él.

# Instrucciones:
# Escribe un bucle for que recorra cada par clave:valor de europe. En cada iteración, debe imprimirse
# "the capital of x is y", donde X es la clave e Y es el valor del par.

# Definition of dictionary
europe = {'spain':'madrid', 'france':'paris', 'germany':'berlin',
          'norway':'oslo', 'italy':'rome', 'poland':'warsaw', 'austria':'vienna' }

# Iterate over europe
for key, value in europe.items() :
    print("the capital of " + key + " is " + value)

# ------------------------------------------------
# Sección 2: Bucle por una matriz NumPy
# ------------------------------------------------
# Si tratas con una matriz NumPy 1D, hacer un bucle por todos los elementos puede ser tan sencillo como:
#
#   for x in my_array :
#       ...
#
# Si se trata de una matriz NumPy 2D, es más complicado. Una matriz 2D está formada por varias matrices 1D.
# Para iterar explícitamente por todos los elementos separados de una matriz multidimensional, necesitarás
# esta sintaxis:
#
#   for x in np.nditer(my_array) :
#       ...
#
# Dos matrices NumPy que quizá reconozcas del curso de introducción están disponibles en tu sesión de
# Python: np_height, una matriz NumPy que contiene las alturas (primera columna) como los jugadores de la Major League
# Baseball, y np_baseball, una matriz NumPy 2D que contiene tanto las alturas (primera columna) como los
# pesos (segunda columna) de los jugadores.

# Instrucciones:
# - Importa el paquete numpy con el alias local np.
# - Escribe un bucle for que itere por todos los elementos de np_height e imprima "x inches" por cada
#   elemento, donde X es el valor de la matriz.
# - Escribe un bucle for que visite cada elemento de la matriz np_baseball y lo imprima.

# Import numpy as np
import numpy as np

# For loop over np_height
np_height = np.array([74, 74, 72, 72, 73, 69, 69, 71, 76, 71])
for x in np_height :
    print(str(x) + " inches")

# For loop over np_baseball
np_baseball = np.array([[74, 180], [74, 215], [72, 210], [72, 210], [73, 188]])
for x in np.nditer(np_baseball) :
    print(x)

