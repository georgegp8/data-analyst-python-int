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

# ------------------------------------------------
# Sección 3: Implementa torpeza
# ------------------------------------------------
# Todo este análisis del paseo aleatorio se ha realizado numerosas veces. Sin embargo, no has incluido el
# elemento de torpeza todavía. En el siguiente fragmento de código, este problema se soluciona.
#
# En los ejercicios anteriores, especificaste el número de cada intento con un bucle for. Lo hiciste de esta
# manera:
#
#   for i in range(10) :
#       ...
#
# Este bucle for no tiene más utilidad que repetir el código 10 veces. De hecho, la variable i no se utiliza
# dentro del bucle for. Si sólo te preocupa el número de repeticiones, una forma más elegante para repetir
# el código un número específico de veces es utilizar _ en lugar del nombre de variable de iteración.
#
# En la presente solución, sin embargo, i es útil, porque necesitas crear 20 listas y asignarlas a all_walks.

# Instrucciones:
# - Cambia la función range() para que la simulación se realice 20 veces.
# - Termina la condición if para que step se ponga a 0 si un float aleatorio es menor o igual que 0.005.
#   Utiliza np.random.rand().

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Initialize all_walks
all_walks = []

# Simulate random walk 20 times
for i in range(20) :
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

        # Implement clumsiness
        if np.random.rand() <= 0.005 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Import matplotlib.pyplot as plt
import matplotlib.pyplot as plt
plt.plot(np_aw_t)
plt.show()

# ------------------------------------------------
# Sección 4: Representa la distribución
# ------------------------------------------------
# Todas estas visualizaciones extravagantes nos han desviado. Aún tenemos que resolver el problema del
# millón: ¿Cuáles son las probabilidades de que llegues a 60 escalones de altura en el Empire State Building?
#
# Básicamente, quieres conocer los puntos finales de todos los paseos aleatorios que has simulado. Estos
# puntos finales tienen una determinado distribución que puedes visualizar con un histograma.
#
# Ten en cuenta que, si el código tarda demasiado en ejecutarse, puede que estés creando un histograma de
# los datos equivocados.

# Instrucciones:
# - Para asegurarnos de que tenemos suficientes simulaciones, que se te vaya la cabeza. Simula el paseo
#   aleatorio 500 veces.
# - En np_aw_t, selecciona la última fila. Aquí está el punto final de los 500 paseos aleatorios que has
#   simulado. Guarda esta matriz NumPy como ends.
# - Utiliza plt.hist() para construir un histograma de ends. No olvides plt.show() para visualizar el
#   gráfico.

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Initialize all_walks
all_walks = []

# Simulate random walk 500 times
for i in range(500) :
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

        # Implement clumsiness
        if np.random.rand() <= 0.001 :
            step = 0

        random_walk.append(step)
    all_walks.append(random_walk)

# Create and plot np_aw_t
np_aw_t = np.transpose(np.array(all_walks))

# Select last row from np_aw_t: ends
ends = np_aw_t[-1,:]

# Plot histogram of ends, display plot
import matplotlib.pyplot as plt
plt.hist(ends)
plt.show()


