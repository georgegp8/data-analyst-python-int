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

# ------------------------------------------------
# Sección 2: Bucle por un DataFrame (2)
# ------------------------------------------------
# Los datos de fila que genera iterrows() en cada ejecución son series de pandas. Este formato no es muy
# cómodo de imprimir. Por suerte, puedes seleccionar fácilmente variables de la serie de pandas mediante
# corchetes:
#
#   for lab, row in brics.iterrows() :
#       print(row['country'])

# Instrucciones:
# - Mediante los iteradores lab y row, adapta el código del bucle for de forma que la primera iteración
#   imprima "US: 809", la segunda iteración "AUS: 731", y así sucesivamente.
# - El resultado debe tener la forma "country: cars_per_cap". Asegúrate de imprimir esta cadena exacta
#   (con el espaciado correcto).
#
# Puedes utilizar str() para convertir los datos enteros en una cadena, de modo que puedas imprimirlos
# junto con la etiqueta del país.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Adapt for loop
for lab, row in cars.iterrows() :
    print(lab + ": " + str(row['cars_per_cap']))

