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

# ------------------------------------------------
# Sección 2: Conducir por la derecha (2)
# ------------------------------------------------
# El código del ejemplo anterior funcionaba bien, pero en realidad ha creado innecesariamente una nueva
# variable dr. Puedes conseguir el mismo resultado sin esta variable intermedia. Pon en el código que calcula
# dr directamente en los corchetes que seleccionan las observaciones de cars.

# Instrucciones:
# Convierte el código en una sola línea que calcule la variable sel como antes.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Convert code to a one-liner
sel = cars[cars['drives_right']]

# Print sel
print(sel)

# ------------------------------------------------
# Sección 3: Coches per cápita (1)
# ------------------------------------------------
# Ciñámonos un poco más a los datos de cars. Esta vez quieres averiguar qué países tienen una cifra
# elevada de coches per cápita. En otras palabras, ¿en qué países tiene mucha gente un coche, o tal vez varios
# coches?
#
# Al igual que en el ejemplo anterior, querrás construir una serie booleana, que luego podrás utilizar para
# subdividir el DataFrame cars para seleccionar determinadas observaciones. Si quieres hacerlo en una sola
# línea, ¡está perfectamente bien!

# Instrucciones:
# - Selecciona la columna cars_per_cap de cars como una serie de pandas y guárdala como cpc.
# - Utiliza cpc en combinación con un operador de comparación y 500. Quieres acabar con una serie
#   booleana que sea True si el país correspondiente tiene un cars_per_cap superior a 500 y False en
#   caso contrario. Guarda esta serie booleana como many_cars.
# - Utiliza many_cars para subconjuntar cars, de forma similar a lo que hiciste antes. Guarda el resultado
#   como car_maniac.
# - Imprime car_maniac para ver si lo has hecho bien.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col = 0)

# Create car_maniac: observations that have a cars_per_cap over 500
cpc = cars['cars_per_cap']
many_cars = cpc > 500
car_maniac = cars[many_cars]

# Print car_maniac
print(car_maniac)

