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

# ------------------------------------------------
# Sección 2: Tira los dados
# ------------------------------------------------
# En el ejercicio anterior, utilizaste rand(), que genera un float aleatorio entre 0 y 1.
#
# Como explica Hugo en el vídeo, también puedes utilizar randint(), también una función del paquete
# random, para generar números enteros aleatoriamente. La siguiente llamada genera aleatoriamente el
# número entero 4, 5, 6 o 7. 8 no está incluido.
#
#   import numpy as np
#   np.random.randint(4, 8)
#
# NumPy ya se ha importado como np y se ha establecido un valor de inicialización.
# ¿Puedes tirar los dados?

# Instrucciones:
# - Utiliza randint() con los argumentos adecuados para generar aleatoriamente el número entero 1, 2, 3, 4,
#   5 o 6. Esto simula un dado. Imprímelo.
# - Repite el resultado para ver si el segundo lanzamiento es diferente. De nuevo, imprime el resultado.

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))
