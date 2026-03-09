# ================================================
# Ejercicios Pandas - Part 1
# ================================================

# ------------------------------------------------
# Sección 1: De diccionario a DataFrame (1)
# ------------------------------------------------
# Pandas es una biblioteca de código abierto que proporciona estructuras de datos y herramientas
# de análisis de datos de alto rendimiento y fáciles de usar para Python.
# El DataFrame es una de las estructuras de datos más importantes de Pandas. Es una forma de
# almacenar datos tabulares en los que puedes etiquetar las filas y las columnas.
# Una forma de construir un DataFrame es a partir de un diccionario.
# Cada clave del diccionario es una etiqueta de columna y cada valor es una lista con los
# elementos de la columna.

# Instrucciones:
# - Importa pandas como pd.
# - Utiliza las listas predefinidas para crear un diccionario llamado my_dict. Debe haber tres pares de clave y valor:
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
# El código Python que resuelve el ejercicio anterior está incluido en el script.
# Las etiquetas de las filas se han establecido automáticamente en números enteros de 0 a 6.
# Para solucionarlo se ha creado una lista row_labels. Puedes utilizarla para especificar
# las etiquetas de las filas del DataFrame cars estableciendo el atributo index de cars.

# Instrucciones:
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
