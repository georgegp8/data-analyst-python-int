# ================================================
# Ejercicios Matplotlib - Gráfico Histograma
# ================================================

# ------------------------------------------------
# Sección 1: Primer histograma
# ------------------------------------------------
# Bienvenido al ejercicio de histogramas. Con los datos de life_exp
# construirás un histograma.

# Instrucciones:
# - Usa plt.hist() para crear un histograma de los valores en life_exp.
#   No uses keyword arguments aún.
# - Añade plt.show() para imprimir el gráfico.

import matplotlib.pyplot as plt

life_exp = [43.828, 76.423, 72.301, 42.731, 75.32, 81.235, 79.829, 75.635, 64.062, 79.441,
            56.728, 65.554, 74.852, 50.728, 72.39, 73.005, 52.295, 49.58, 59.723, 50.43,
            80.653, 44.74100000000001, 50.651, 78.553, 72.961, 72.889, 65.152, 46.462,
            55.322, 78.782, 48.328, 75.748, 78.273, 76.486, 78.332, 54.791, 72.235, 74.994,
            71.33800000000001, 71.878, 51.57899999999999, 58.04, 52.947, 79.313, 80.657,
            56.735, 59.448, 79.406, 60.022, 79.483, 70.259, 56.007, 46.388000000000005,
            60.916, 70.19800000000001, 82.208, 73.33800000000001, 81.757, 64.69800000000001,
            70.65, 70.964, 59.545, 78.885, 80.745, 80.546, 72.567, 82.603, 72.535, 54.11,
            67.297, 78.623, 77.58800000000001, 71.993, 42.592, 45.678, 73.952, 59.443000000000005,
            48.303, 74.241, 54.467, 64.164, 72.801, 76.195, 66.803, 74.543, 71.164, 42.082,
            62.069, 52.906000000000006, 63.785, 79.762, 80.204, 72.899, 56.867, 46.859,
            80.196, 75.64, 65.483, 75.53699999999999, 71.752, 71.421, 71.688, 75.563,
            78.098, 78.74600000000001, 76.442, 72.476, 46.242, 65.528, 72.777, 63.062,
            74.002, 42.568000000000005, 79.972, 74.663, 77.926, 48.159, 49.339, 80.941,
            72.396, 58.556, 39.613, 80.884, 81.70100000000001, 74.143, 78.4, 52.517,
            70.616, 58.42, 69.819, 73.923, 71.777, 51.542, 79.425, 78.242, 76.384,
            73.747, 74.249, 73.422, 62.698, 42.38399999999999, 43.487]

# Crear histograma con los datos de life_exp
plt.hist(life_exp)

# Mostrar el histograma
plt.show()

# ------------------------------------------------
# Sección 2: Construye un histograma (2): barras
# ------------------------------------------------
# En el ejercicio anterior, no especificaste el número de barras. De forma predeterminada,
# Python establece el número de barras en 10 en ese caso. El número de barras es bastante
# importante. Si hay demasiadas pocas barras, simplificarán demasiado la realidad y no te
# mostrarán los detalles. Demasiadas barras complicarán demasiado la realidad y no mostrarán
# el panorama general.
# Para controlar el número de barras en las que dividir los datos, puedes establecer el argumento bins.
# plt.show() muestra un gráfico y plt.clf() lo vuelve a limpiar para que puedas empezar de nuevo.

# Instrucciones:
# - Construye un histograma de life_exp con 5 barras. ¿Puedes decir qué papelera contiene más observaciones?
# - Construye otro histograma de life_exp, esta vez con 20 barras. ¿Mejor?

# Construir histograma con 5 barras
plt.hist(life_exp, bins=5)

# Mostrar y limpiar el gráfico
plt.show()
plt.clf()

# Construir histograma con 20 barras
plt.hist(life_exp, bins=20)

# Mostrar y limpiar de nuevo
plt.show()
plt.clf()
