# ================================================
# Caso Práctico: Caminatas Aleatorias
# Ejercicios: Paseo Aleatorio
# ================================================

# ------------------------------------------------
# Sección 1: El siguiente paso
# ------------------------------------------------
# Antes, ya has escrito el código Python que determina el paso siguiente en función del paso anterior.
# Ahora es el momento de poner este código dentro de un bucle for para que podamos simular un
# paseo aleatorio.

# Instrucciones:
# - Haz una lista random_walk que contenga el primer paso, que es el entero 0.
# - Termina el bucle for:
#   - El bucle debe ejecutarse 100 veces.
#   - En cada iteración, establece step igual al último elemento de la lista random_walk.
#     Para ello puedes utilizar el índice -1.
#   - A continuación, deja que la construcción if - elif - else actualice step por ti.
# - El código que añade step a random_walk ya está codificado.
# - Imprime random_walk.

# Import numpy as np
import numpy as np

# Set the seed
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

# Complete the for loop
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = step - 1
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # Append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)

# ------------------------------------------------
# Sección 2: ¿Hasta dónde puedes llegar?
# ------------------------------------------------
# Las cosas van tomando forma. Ya tienes un código que calcula tu ubicación en el Empire State Building
# después de 100 lanzamientos de dados. Sin embargo, hay algo en lo que no hemos pensado: no puedes bajar
# de 0.
#
# Una forma típica de resolver problemas como éste es utilizar max(). Si pasas a max() dos argumentos, se
# devuelve el mayor. Por ejemplo, para asegurarte de que una variable x nunca baje de 10 cuando la
# disminuyas, puedes utilizar:
#
#   x = max(10, x - 1)

# Instrucciones:
# - max() de forma similar para asegurarte de que step no baje de cero si dice <= 2.
# - Pulsa Enviar respuesta y comprueba el contenido de random_walk.

# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Initialize random_walk
random_walk = [0]

# Complete the for loop
for x in range(100) :
    # Set step: last element in random_walk
    step = random_walk[-1]

    # Roll the dice
    dice = np.random.randint(1,7)

    # Determine next step
    if dice <= 2:
        step = max(0, step - 1)
    elif dice <= 5:
        step = step + 1
    else:
        step = step + np.random.randint(1,7)

    # Append next_step to random_walk
    random_walk.append(step)

# Print random_walk
print(random_walk)
