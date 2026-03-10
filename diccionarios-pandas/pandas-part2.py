# ================================================
# Ejercicios Pandas - Part 2
# ================================================

# ------------------------------------------------
# Sección 1: Corchetes (1)
# ------------------------------------------------
# Hay varias maneras de indexar un DataFrame de Pandas. Una de las maneras más eficaces es
# utilizar corchetes.
# En el siguiente ejemplo, puedes seleccionar la columna country así:
# cars['country']
# Pruébalo en el shell para ver si funciona. Si lo haces, te darás cuenta de que seleccionar
# una columna con un único corchete devuelve un objeto Pandas Series. Para seleccionar la
# columna country como un DataFrame, puedes utilizar:
# cars[['country']]
# El código de ejemplo utiliza corchetes dobles.

# Instrucciones:
# - Utiliza corchetes simples para imprimir la columna drives_right de cars como una Serie.
# - Utiliza corchetes dobles para imprimir la columna drives_right de cars como un DataFrame.

import pandas as pd

cars = pd.read_csv('cars.csv', index_col=0)

# Print out drives_right column as Pandas Series
print(cars['drives_right'])

# Print out drives_right column as Pandas DataFrame
print(cars[['drives_right']])
