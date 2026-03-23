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
