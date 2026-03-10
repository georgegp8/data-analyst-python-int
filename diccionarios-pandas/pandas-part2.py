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

# ------------------------------------------------
# Sección 2: Corchetes (2)
# ------------------------------------------------
# Los corchetes pueden hacer algo más que seleccionar columnas. También puedes utilizarlos para
# obtener filas, u observaciones, de un DataFrame. La siguiente llamada selecciona las cinco
# primeras filas del DataFrame cars:
# cars[0:5]
# El resultado es otro DataFrame que solo contiene las filas que has especificado.
# Presta atención: solo puedes seleccionar filas mediante corchetes si especificas un segmento,
# como 0:4. Además, aquí estás utilizando los índices enteros de las filas, ¡no las etiquetas
# de las filas!

# Instrucciones:
# - Selecciona las 3 primeras observaciones de cars e imprimelas.
# - Selecciona la cuarta, quinta y sexta observación, correspondientes a los índices de fila 3,
#   4 y 5, e imprimelas.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Print out first 3 observations
print(cars[0:3])

# Print out fourth, fifth and sixth observation
print(cars[3:6])

# ------------------------------------------------
# Sección 3: loc e iloc (1)
# ------------------------------------------------
# Con loc y iloc puedes hacer prácticamente cualquier operación de selección de datos en
# DataFrames que se te ocurra. loc se basa en etiquetas, lo que significa que tienes que
# especificar filas y columnas en función de las etiquetas de fila y columna. iloc se basa en
# índices enteros, por lo que tienes que especificar filas y columnas por su índice entero,
# como hiciste en el ejercicio anterior.
# Prueba los siguientes comandos para experimentar con loc y iloc para seleccionar
# observaciones. Cada par de comandos da el mismo resultado.
#
# cars.loc['RU']
# cars.iloc[4]
#
# cars.loc[['RU']]
# cars.iloc[[4]]
#
# cars.loc[['RU', 'AUS']]
# cars.iloc[[4, 1]]
#
# Como antes, se incluye código que importa los datos de los coches como un DataFrame de pandas.

# Instrucciones:
# - Utiliza loc o iloc para seleccionar la observación correspondiente a Japón como una serie.
#   La etiqueta de esta fila es JPN, el índice es 2. Asegúrate de imprimir la serie resultante.
# - Utiliza loc o iloc para seleccionar las observaciones de Australia y Egipto como un
#   DataFrame. Puedes averiguar las etiquetas/índices de estas filas si inspeccionas cars.
#   Asegúrate de imprimir el DataFrame resultante.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Print out observation for Japan
print(cars.loc['JPN'])

# Print out observations for Australia and Egypt
print(cars.iloc[[1, 6]])

# ------------------------------------------------
# Sección 4: loc e iloc (2)
# ------------------------------------------------
# loc e iloc también te permiten seleccionar tanto filas como columnas de un DataFrame. Para
# experimentar, prueba los siguientes comandos. De nuevo, los comandos emparejados producen el
# mismo resultado.
#
# cars.loc['IN', 'cars_per_cap']
# cars.iloc[3, 0]
#
# cars.loc[['IN', 'RU'], 'cars_per_cap']
# cars.iloc[[3, 4], 0]
#
# cars.loc[['IN', 'RU'], ['cars_per_cap', 'country']]
# cars.iloc[[3, 4], [0, 1]]

# Instrucciones:
# - Imprime el valor drives_right de la fila correspondiente a Marruecos (su etiqueta de fila
#   es MOR).
# - Imprime un subDataFrame que contenga las observaciones de Rusia y Marruecos y las columnas
#   country y drives_right.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Print out drives_right value of Morocco
print(cars.loc['MOR', 'drives_right'])

# Print sub-DataFrame
print(cars.iloc[[4, 5], [1, 2]])

# ------------------------------------------------
# Sección 5: loc e iloc (3)
# ------------------------------------------------
# También es posible seleccionar solo las columnas con loc y iloc. En ambos casos, basta con
# poner delante de la coma un segmento que abarque del principio al final:
#
# cars.loc[:, 'country']
# cars.iloc[:, 1]
#
# cars.loc[:, ['country','drives_right']]
# cars.iloc[:, [1, 2]]

# Instrucciones:
# - Imprime la columna drives_right como una serie utilizando loc o iloc.
# - Imprime la columna drives_right como un DataFrame utilizando loc o iloc.
# - Imprime las columnas cars_per_cap y drives_right como un DataFrame utilizando loc o iloc.

# Import cars data
import pandas as pd
cars = pd.read_csv('cars.csv', index_col=0)

# Print out drives_right column as Series
print(cars.loc[:, 'drives_right'])

# Print out drives_right column as DataFrame
print(cars.iloc[:, [2]])

# Print out cars_per_cap and drives_right as DataFrame
print(cars.loc[:, ['cars_per_cap', 'drives_right']])
