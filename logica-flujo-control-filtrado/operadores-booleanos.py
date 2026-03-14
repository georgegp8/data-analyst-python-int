# ================================================
# Lógica, Flujo de Control y Filtrado
# Ejercicios: Operadores Booleanos
# ================================================

# ------------------------------------------------
# Sección 1: and, or, no
# ------------------------------------------------
# Antes de ir más lejos, hay que hablar de los operadores booleanos and, or y not.
# Los operadores booleanos son fundamentales para crear condiciones más complejas.
#
# - and: devuelve True solo si ambas condiciones son True.
# - or: devuelve True si al menos una de las condiciones es True.
# - not: invierte el valor booleano (True se convierte en False y viceversa).
#
# Estos son algunos ejemplos que dan como resultado True:
#
#   True and True
#   False or True
#   not False

# Instrucciones:
# - Escribe código Python para comprobar si my_kitchen es más grande que 10
#   y también más pequeño que 18. Imprime el resultado.
# - Escribe código para ver si my_kitchen es más pequeño que 14 o más grande
#   que 17. Imprime el resultado.
# - ¿El doble de my_kitchen es menor que el triple de your_kitchen? Imprímelo.

# Define variables
my_kitchen = 18.0
your_kitchen = 14.0

# my_kitchen bigger than 10 and smaller than 18?
print(my_kitchen > 10 and my_kitchen < 18)

# my_kitchen smaller than 14 or bigger than 17?
print(my_kitchen < 14 or my_kitchen > 17)

# Double my_kitchen smaller than triple your_kitchen?
print(my_kitchen * 2 < your_kitchen * 3)

# ------------------------------------------------
# Sección 2: Booleanos sobre arrays
# ------------------------------------------------
# Antes de continuar, hagamos un breve repaso. Para utilizar operadores booleanos
# con matrices NumPy, necesitas np.logical_and(), np.logical_or() y np.logical_not().
#
# Aquí tienes un ejemplo del uso de np.logical_and() con NumPy:
#
#   np.logical_and(bmi > 21, bmi < 22)
#
# Recuerda que bmi fue definido en la sección anterior.

# Instrucciones:
# - Genera una matriz booleana que indique en qué habitaciones la superficie
#   de my_house es mayor que 18.5 o menor que 10.
# - Genera una matriz booleana que indique en qué habitaciones my_house
#   es menor que 11 al mismo tiempo que your_house es mayor que 15.
# - Imprime ambos resultados.

import numpy as np

my_house = np.array([18.0, 20.0, 10.75, 9.50])
your_house = np.array([14.0, 24.0, 14.25, 9.0])

# my_house greater than 18.5 or smaller than 10
print(np.logical_or(my_house > 18.5, my_house < 10))

# Both my_house and your_house smaller than 11
print(np.logical_and(my_house < 11, your_house < 11))

# ------------------------------------------------
# Sección 3: if, elif, else
# ------------------------------------------------
# Es hora de hacer algo interesante con tus valores. En el vídeo, Hugo habló de
# la sentencia if en Python. Tiene la siguiente sintaxis:
#
#   if condition :
#       expression
#
# Si la condición se evalúa como verdadera, se ejecuta la expresión. Si la condición
# es False, la expresión se omite y Python continúa.
#
# Es posible incluir la sentencia elif y else para especificar condiciones adicionales
# y acciones para cuando las condiciones anteriores no se cumplan.

# Instrucciones:
# - Examina el código de la muestra e intenta entender qué hace.
# - Imprime el resultado de la expresión if-elif-else.

# Define variables
room = "kit"
area = 14.0

# if-elif-else construct for room
if room == "kit":
    print("looking around in the kitchen.")
elif room == "bed":
    print("looking around in the bedroom.")
else:
    print("looking around elsewhere.")

# if-elif-else construct for area
if area > 15:
    print("big place!")
elif area > 10:
    print("medium place!")
else:
    print("small place!")
