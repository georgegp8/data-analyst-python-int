# ================================================
# Lógica, Flujo de Control y Filtrado
# Ejercicios: Filtrar pandas DataFrames
# ================================================

# ------------------------------------------------
# Sección 1: Conducir por la derecha (1)
# ------------------------------------------------
# En las carpetas Working With Columns y Filtering Rows, aprendiste los fundamentos
# de la selección de subdivisiones de un DataFrame. Para filtrar las filas de observaciones
# basándote en una determinada condición, combinas ambas técnicas: selecciona una columna
# de interés y crea una matriz booleana que codifique esa condición, y luego utiliza
# esta matriz booleana dentro de corchetes para hacer la subdivisión.
#
# El conjunto de datos cars contiene coches por cada 1000 personas (cars_per_cap) y si la gente
# conduce por la derecha (drives_right), además del nombre del país (country) para cada observación.
#
# En este ejercicio encontrarás todas las observaciones en cars donde drives_right es True.
# drives_right es una columna booleana, por lo que tendrás que extraerla como Serie y luego
# utilizar esta Serie booleana para seleccionar observaciones de cars.

# Instrucciones:
# - Extrae la columna drives_right como una Serie de Pandas y almacénala como dr.
# - Utiliza dr, una Serie booleana, para subdividir el DataFrame cars. Guarda la selección resultante en sel.
# - Imprime sel, y afirma que drives_right es True en todas las observaciones.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Extract drives_right column as Series: dr
dr = cars['drives_right']

# Use dr to subset cars: sel
sel = cars[dr]

# Print sel
print(sel)
