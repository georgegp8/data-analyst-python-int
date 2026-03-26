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

# ------------------------------------------------
# Sección 2: Visualiza todos los paseos
# ------------------------------------------------
# all_walks es una lista de listas: cada sublista representa un único paseo aleatorio. Si conviertes esta lista de
# listas en una matriz NumPy, podrás empezar a hacer gráficos interesantes. matplotlib.pyplot ya se ha
# importado como plt.
#
# El bucle anidado for ya se ha programado; no te preocupes. De momento, céntrate en el código que viene
# después de este bucle for.

# Instrucciones:
# - Utiliza np.array() para convertir all_walks en una matriz NumPy, np_aw.
# - Intenta utilizar plt.plot() en np_aw. Incluye también plt.show() .¿Ya funciona?
# - Transpón np_aw mediante la llamada a np.transpose() en np_aw. Llama al resultado np_aw_t. Llama a
#   plt.plot() de nuevo con este np_aw_t y muéstralo. ¿Mejor?

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

# Convert all_walks to NumPy array: np_aw
np_aw = np.array(all_walks)

# Plot np_aw and show
import matplotlib.pyplot as plt
plt.plot(np_aw)
plt.show()

# Clear the figure
plt.clf()

# Transpose np_aw: np_aw_t
np_aw_t = np.transpose(np_aw)

# Plot np_aw_t and show
plt.plot(np_aw_t)
plt.show()

