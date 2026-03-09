# ================================================
# Ejercicios Diccionarios - Part 2
# ================================================

# ------------------------------------------------
# Sección 1: Manipulación del diccionario (1)
# ------------------------------------------------
# Si sabes cómo acceder a un diccionario, también puedes asignarle un nuevo valor.
# Para añadir un nuevo par clave-valor a europe puedes utilizar algo como esto:
# europe['iceland'] = 'reykjavik'

# Instrucciones:
# - Añade la clave 'italy' con el valor 'rome' a europe.
# - Para afirmar que 'italy' es ahora una clave en europe, imprime 'italy' in europe.
# - Añade otro par clave:valor a europe: 'poland' es la clave, 'warsaw' es el valor correspondiente.
# - Imprime europe.

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'berlin', 'norway': 'oslo'}

# Add italy to europe
europe['italy'] = 'rome'

# Print out italy in europe
print('italy' in europe)

# Add poland to europe
europe['poland'] = 'warsaw'

# Print europe
print(europe)

# ------------------------------------------------
# Sección 2: Manipulación del diccionario (2)
# ------------------------------------------------
# Alguien ha pensado que sería divertido meterse con tu diccionario generado con precisión.
# Dispones de una versión adaptada del diccionario europe en el script.
# ¿Puedes limpiarlo? Para ello, no adaptes la definición de europe, sino que tienes que
# añadir comandos Python al script para actualizar y eliminar pares clave:valor.

# Instrucciones:
# - La capital de Alemania ("Germany" en inglés) no es 'bonn'; es 'berlin'. Actualiza su valor.
# - Australia no está en Europa, Austria sí. Elimina la clave 'australia' de europe.
# - Imprime europe para ver si tu trabajo de limpieza ha merecido la pena.

# Definition of dictionary
europe = {'spain': 'madrid', 'france': 'paris', 'germany': 'bonn',
          'norway': 'oslo', 'italy': 'rome', 'poland': 'warsaw',
          'australia': 'vienna'}

# Update capital of germany
europe['germany'] = 'berlin'

# Remove australia
del(europe['australia'])

# Print europe
print(europe)

# ------------------------------------------------
# Sección 3: Diccionarización
# ------------------------------------------------
# ¿Recuerdas las listas? Pueden contener cualquier cosa, incluso otras listas. Pues con los
# diccionarios ocurre lo mismo. Los diccionarios pueden contener pares clave:valor en los que
# los valores son de nuevo diccionarios.
# Las claves siguen siendo los nombres de los países, pero los valores son diccionarios que
# contienen más información que la capital.
# Es perfectamente posible encadenar corchetes para seleccionar elementos.
# Para obtener la población de España en europe, por ejemplo, necesitas: europe['spain']['population']

# Instrucciones:
# - Utiliza corchetes encadenados para seleccionar e imprimir la capital de Francia.
# - Crea un diccionario, denominado data, con las claves 'capital' y 'population'. Fíjalos en 'rome' y 59.83, respectivamente.
# - Añade un nuevo par clave-valor a europe; la clave es 'italy' y el valor es data, el diccionario que acabas de construir.

# Dictionary of dictionaries
europe = {'spain': {'capital': 'madrid', 'population': 46.77},
          'france': {'capital': 'paris', 'population': 66.03},
          'germany': {'capital': 'berlin', 'population': 80.62},
          'norway': {'capital': 'oslo', 'population': 5.084}}

# Print out the capital of France
print(europe['france']['capital'])

# Create sub-dictionary data
data = {'capital': 'rome', 'population': 59.83}

# Add data to europe under key 'italy'
europe['italy'] = data

# Print europe
print(europe)
