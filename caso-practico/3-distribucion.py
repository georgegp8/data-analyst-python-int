# ================================================
# Caso Práctico: Caminatas Aleatorias
# Ejercicios: Distribución
# ================================================

# ------------------------------------------------
# Sección 1: Simular varios paseos
# ------------------------------------------------
# Un paseo aleatorio sigue siendo sólo una salida de un proceso aleatorio. Tendrás que repetir el paseo
# aleatorio muchas veces para conseguir una comprensión aceptable del proceso.
#
# Si repites esto varias veces, podrías empezar a analizar los paseos aleatorios.
#
# Termina la construcción for anidada:
#   - El exterior for debe iterar sobre todos_walks.
#   - El interior for debe iterar sobre random_walk, salida del paseo aleatorio.

# Instrucciones:
# - Rellena la especificación del bucle for de forma que el paseo aleatorio se simule cinco veces.
# - Cuando la matriz random_walk esté totalmente tramitada, añádela a la lista all_walks.
# - Por último, después del bucle for de nivel superior, imprime all_walks.

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Initialize all_walks (don't change this line)
all_walks = []

# Simulate random walk 5 times
for i in range(5) :

    # Code from before
    random_walk = [0]
    for x in range(100) :
        step = random_walk[-1]
        dice = np.random.randint(1,7)

        if dice <= 2:
            step = max(0, step - 1)
        elif dice <= 5:
            step = step + 1
        else:
            step = step + np.random.randint(1,7)
        random_walk.append(step)

    # Append random_walk to all_walks
    all_walks.append(random_walk)

# Print all_walks
print(all_walks)
