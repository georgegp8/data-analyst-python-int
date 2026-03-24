# ================================================
# Caso Práctico: Caminatas Aleatorias
# Ejercicios: Números Aleatorios
# ================================================

# ------------------------------------------------
# Sección 1: Float aleatorio
# ------------------------------------------------
# El azar tiene muchos usos en la ciencia, el arte, la estadística, la criptografía, el juego,
# las apuestas y otros campos. Vas a utilizar el azar para simular un juego.
#
# Toda la funcionalidad que necesitas está contenida en el paquete random, un subpaquete de numpy.
# En este ejercicio, utilizarás dos funciones de este paquete:
#
# - seed(): establece el valor de inicialización aleatorio, para que tus resultados sean
#   reproducibles entre simulaciones. Como argumento, toma un número entero de tu elección.
#   Si llamas a la función, no se generará ninguna salida.
# - rand(): si no especificas ningún argumento, genera un float aleatorio entre cero y uno.

# Instrucciones:
# - Importa numpy como np.
# - Utiliza seed() para establecer el valor de inicialización; como argumento, pasa 123.
# - Genera tu primer float aleatorio con rand() e imprímelo.

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Generate and print random float
print(np.random.rand())
