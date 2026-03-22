# ================================================
# Bucles
# Ejercicios: for
# ================================================

# ------------------------------------------------
# Sección 1: Bucle por una lista
# ------------------------------------------------
# Echa otro vistazo al bucle for que Hugo mostró en el vídeo:
#
#   fam = [1.73, 1.68, 1.71, 1.89]
#   for height in fam :
#       print(height)
#
# Como de costumbre, solo tienes que sangrar el código con 4 espacios para indicar a Python
# qué código debe ejecutarse en el bucle for.
#
# La variable areas, que contiene la superficie de las distintas habitaciones de la casa,
# ya está definida.

# Instrucciones:
# Escribe un bucle for que itere sobre todos los elementos de la lista areas e imprima
# cada elemento por separado.

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Code the for loop
for area in areas :
    print(area)

# ------------------------------------------------
# Sección 2: Índices y valores (1)
# ------------------------------------------------
# Utilizar un bucle for para iterar por una lista solo te da acceso a cada elemento de la lista en cada
# ejecución, uno tras otro. Si también quieres acceder a la información del índice, es decir, dónde se encuentra
# el elemento de la lista sobre el que estás iterando, puedes utilizar enumerate().
#
# Como ejemplo, mira cómo se convirtió el bucle for del vídeo:
#
#   fam = [1.73, 1.68, 1.71, 1.89]
#   for index, height in enumerate(fam) :
#       print("person " + str(index) + ": " + str(height))

# Instrucciones:
# - Adapta el bucle for del código de ejemplo para utilizar enumerate() y utilizar dos variables de iteración.
# - Actualiza la declaración print() para que en cada ejecución se imprima una línea de la forma
#   "room x: y", donde X es el índice del elemento de la lista e Y es el elemento real de la lista, es decir, el
#   área. Asegúrate de imprimir esta cadena exacta, con el espaciado correcto.

# areas list
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Change for loop to use enumerate() and update print()
for index, area in enumerate(areas) :
    print("room " + str(index) + ": " + str(area))

