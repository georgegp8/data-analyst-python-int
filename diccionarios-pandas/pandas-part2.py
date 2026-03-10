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
