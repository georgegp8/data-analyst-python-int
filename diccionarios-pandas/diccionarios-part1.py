# ================================================
# Ejercicios Diccionarios - Part 1
# ================================================

# ------------------------------------------------
# Sección 1: Motivación de los diccionarios
# ------------------------------------------------
# Para ver por qué son útiles los diccionarios, echa un vistazo a las dos listas definidas en el script.
# countries contiene los nombres de algunos países europeos.
# capitals enumera los nombres correspondientes de sus capitales.

# Instrucciones:
# - Utiliza el método index() en countries para hallar el índice de 'germany'. Guarda este índice como ind_ger.
# - Utiliza ind_ger para acceder a la capital de Alemania desde la lista capitals. Imprímelo.

# Definición de países y capitales
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# Obtener el índice de 'germany': ind_ger
ind_ger = countries.index('germany')

# Usar ind_ger para imprimir la capital de Alemania
print(capitals[ind_ger])

# ------------------------------------------------
# Sección 2: Cómo crear un diccionario
# ------------------------------------------------
# Las listas countries y capitals vuelven a estar disponibles en el script.
# Tu trabajo consiste en convertir estos datos en un diccionario en el que
# los nombres de los países sean las claves y las capitales los valores correspondientes.

# Instrucciones:
# - Con las cadenas de countries y capitals, crea un diccionario llamado europe con 4 pares clave:valor.
#   ¡Cuidado con las mayúsculas! Asegúrate de utilizar minúsculas en todas partes.
# - Imprime europe para ver si el resultado es el esperado.

# Definición de países y capitales
countries = ['spain', 'france', 'germany', 'norway']
capitals = ['madrid', 'paris', 'berlin', 'oslo']

# A partir de las cadenas de countries y capitals, crear el diccionario europe
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo'}

# Imprimir europe
print(europe)

# ------------------------------------------------
# Sección 3: Cómo acceder al diccionario
# ------------------------------------------------
# Si las claves de un diccionario se eligen sabiamente, acceder a los valores es fácil e intuitivo.
# Por ejemplo, para obtener la capital de Francia de europe puedes utilizar: europe['france']
# Aquí, 'france' es la clave y 'paris' el valor devuelto.

# Instrucciones:
# - Comprueba qué claves están en europe a través de una llamada al método keys() en europe. Imprime el resultado.
# - Imprime el valor que pertenece a la clave 'norway'.

# Definición del diccionario
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo'}

# Imprimir las claves de europe
print(europe.keys())

# Imprimir el valor que pertenece a la clave 'norway'
print(europe['norway'])


