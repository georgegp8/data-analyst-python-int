# ================================================
# Ejercicios Pandas - Part 1
# ================================================

# ------------------------------------------------
# Sección 1: De diccionario a DataFrame (1)
# ------------------------------------------------
# Pandas es una biblioteca de código abierto que proporciona estructuras de datos y herramientas
# de análisis de datos de alto rendimiento y fáciles de usar para Python. ¡Suena prometedor!
# El DataFrame es una de las estructuras de datos más importantes de Pandas. Básicamente, es una
# forma de almacenar datos tabulares en los que puedes etiquetar las filas y las columnas. Una
# forma de construir un DataFrame es a partir de un diccionario.
# En los ejercicios que siguen trabajarás con datos de vehículos de distintos países. Cada
# observación corresponde a un país y las columnas dan información sobre el número de vehículos
# per cápita, si la gente conduce por la izquierda o por la derecha, etc.
# En el script se definen tres listas:
# - names, que contiene los nombres de los países de los que se dispone de datos.
# - dr, una lista con booleanos que indica si la gente conduce por la izquierda o por la derecha
#   en el país correspondiente.
# - cpc, el número de vehículos de motor por cada 1000 habitantes en el país correspondiente.
# Cada clave del diccionario es una etiqueta de columna y cada valor es una lista que contiene
# los elementos de la columna.

# Instrucciones:
# - Importa pandas como pd.
# - Utiliza las listas predefinidas para crear un diccionario llamado my_dict. Debe haber tres
#   pares de clave y valor:
#   clave 'country' y valor names
#   clave 'drives_right' y valor dr
#   clave 'cars_per_cap' y valor cpc
# - Utiliza pd.DataFrame() para convertir tu diccionario en un DataFrame llamado cars.
# - Imprime cars y verás qué bonito es.

# Pre-defined lists
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]

# Import pandas as pd
import pandas as pd

# Create dictionary my_dict with three key:value pairs: my_dict
my_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}

# Build a DataFrame cars from my_dict: cars
cars = pd.DataFrame(my_dict)

# Print cars
print(cars)

# ------------------------------------------------
# Sección 2: De diccionario a DataFrame (2)
# ------------------------------------------------
# El código Python que resuelve el ejercicio anterior está incluido en el script. ¿Te has dado
# cuenta de que las etiquetas de las filas (es decir, las etiquetas de las distintas
# observaciones) se han establecido automáticamente en números enteros de 0 a 6?
# Para solucionarlo se ha creado una lista row_labels. Puedes utilizarla para especificar las
# etiquetas de las filas del DataFrame cars. Para ello, debes establecer el atributo index de
# cars, al que puedes acceder como cars.index.

# Instrucciones:
# - Pulsa Ejecutar código para ver que, efectivamente, las etiquetas de las filas no están
#   correctamente configuradas.
# - Especifica las etiquetas de las filas estableciendo cars.index igual a row_labels.
# - Vuelve a imprimir cars y comprueba si esta vez las etiquetas de las filas son correctas.

# Build cars DataFrame
names = ['United States', 'Australia', 'Japan', 'India', 'Russia', 'Morocco', 'Egypt']
dr = [True, False, False, False, True, True, True]
cpc = [809, 731, 588, 18, 200, 70, 45]
cars_dict = {'country': names, 'drives_right': dr, 'cars_per_cap': cpc}
cars = pd.DataFrame(cars_dict)
print(cars)

# Definition of row_labels
row_labels = ['US', 'AUS', 'JPN', 'IN', 'RU', 'MOR', 'EG']

# Specify row labels of cars
cars.index = row_labels

# Print cars again
print(cars)

# ------------------------------------------------
# Sección 3: De CSV a DataFrame
# ------------------------------------------------
# Poner los datos en un diccionario y luego construir un DataFrame funciona, pero no es muy
# eficiente. ¿Y si se trata de millones de observaciones? En esos casos, los datos suelen estar
# disponibles como archivos con una estructura regular. Uno de esos tipos de archivo es el
# archivo CSV, que es la abreviatura de «valores separados por comas».
# Para importar datos CSV a Python como un DataFrame de Pandas, puedes utilizar read_csv().
# Exploremos esta función con los mismos datos de los coches de los ejercicios anteriores. Esta
# vez, sin embargo, los datos están disponibles en un archivo CSV, llamado cars.csv. Está
# disponible en tu directorio de trabajo actual, por lo que la ruta al archivo es simplemente
# 'cars.csv'.

# Instrucciones:
# - Para importar archivos CSV, aún necesitas el paquete pandas: impórtalo como pd.
# - Utiliza pd.read_csv() para importar los datos de cars.csv como un DataFrame. Guarda este
#   DataFrame como cars.
# - Imprime cars. ¿Todo parece estar bien?

# Import pandas as pd
import pandas as pd

# Import the cars.csv data: cars
cars = pd.read_csv("cars.csv")

# Print out cars
print(cars)

# ------------------------------------------------
# Sección 4: De CSV a DataFrame (2)
# ------------------------------------------------
# Tu llamada read_csv() para importar los datos CSV no generó ningún error, pero el resultado
# no es exactamente el que queríamos. Las etiquetas de las filas se importaron como otra columna
# sin nombre.
# ¿Recuerdas index_col, un argumento de read_csv(), que puedes utilizar para especificar qué
# columna del archivo CSV debe utilizarse como etiqueta de fila? ¡Pues eso es exactamente lo
# que necesitas aquí!
# El código Python que resuelve el ejercicio anterior ya está incluido; ¿puedes hacer los
# cambios oportunos para arreglar la importación de datos?

# Instrucciones:
# - Ejecuta el código con Ejecutar código y comprueba que la primera columna debe utilizarse
#   realmente como etiquetas de fila.
# - Especifica el argumento index_col dentro de pd.read_csv(): ponlo en 0, para que la primera
#   columna se utilice como etiquetas de fila.
# - ¿Ha mejorado ahora la impresión de cars?

# Import pandas as pd
import pandas as pd

# Fix import by including index_col
cars = pd.read_csv('cars.csv', index_col=0)

# Print out cars
print(cars)
