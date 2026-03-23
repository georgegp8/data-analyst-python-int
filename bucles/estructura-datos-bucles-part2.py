# ================================================
# Bucles
# Ejercicios: Estructuras de Datos - Parte 2
# ================================================

# ------------------------------------------------
# Sección 1: Bucle por un DataFrame (1)
# ------------------------------------------------
# Iterar por un DataFrame de pandas normalmente se hace con el método iterrows(). Se utiliza en cada
# observación de un DataFrame, produciendo en cada iteración tanto una etiqueta como el contenido de toda
# una fila con esta etiqueta. La etiqueta es el nombre de la fila, mientras que la fila en sí es una serie de pandas.
#
# Por ejemplo, considera el siguiente DataFrame:
#
#   brics
#         country    capital  area  population
#   BR     Brazil   Brasília   8.5      200.4
#   RU     Russia     Moscow  17.1      143.5
#   IN      India  New Delhi   3.3     1252.0
#   CH      China    Beijing   9.6     1357.0
#   SA South Africa   Pretoria   1.2       52.9
#
# Puedes utilizar el siguiente código para hacer un bucle por cada línea:
#
#   for lab, row in brics.iterrows() :
#       print(lab)
#       print(row)
#
# En este ejercicio y en los siguientes trabajarás con el DataFrame cars, que contiene información sobre
# coches per cápita y si la gente conduce por la derecha o por la izquierda en siete países del mundo.

# Instrucciones:
# Escribe un bucle for que itere por las filas de cars y en cada iteración realice dos llamadas a print():
# - Imprime la etiqueta de la fila.
# - Imprime todo el contenido de esa fila (todas sus columnas).

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Iterate over rows of cars
for lab, row in cars.iterrows() :
    print(lab)
    print(row)
