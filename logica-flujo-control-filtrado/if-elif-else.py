# ================================================
# Lógica, Flujo de Control y Filtrado
# Ejercicios: Sentencias if, elif, else
# ================================================

# ------------------------------------------------
# Sección 1: Calentamiento
# ------------------------------------------------
# Las sentencias if, elif y else te permiten ejecutar código condicionalmente.
# Puedes crear condiciones más complejas encadenando múltiples sentencias elif.
# Recuerda que solo se ejecuta el bloque de código del primer if o elif que sea verdadero.
#
# En el siguiente ejemplo:
#   - Si area < 9, imprime "small"
#   - Si area < 12, imprime "medium"
#   - Si ninguna condición anterior es verdadera, imprime "large"
#
# Con area = 10.0:
#   - 10.0 < 9 es False (se salta el primer print)
#   - 10.0 < 12 es True (se ejecuta el segundo print)
#   - Resultado: "medium"

# Instrucciones:
# Ejecuta el siguiente código y selecciona qué se imprime en la consola:

area = 10.0

if area < 9 :
    print("small")
elif area < 12 :
    print("medium")
else:
    print("large")

# ¿Qué salida produce este código?
# a) small
# b) medium
# c) large
# d) La sintaxis es incorrecta; este código producirá un error
#
# Respuesta correcta: b) medium

# ------------------------------------------------
# Sección 2: if
# ------------------------------------------------
# Es hora de echar un vistazo a tu casa.
#
# En el código de ejemplo se definen dos variables: room, una cadena que te indica qué habitación de la casa
# estamos viendo, y area, la superficie de esa habitación.

# Instrucciones:
# - Echa un vistazo a la declaración if que imprime "Looking around in the kitchen." si room es igual a "kit".
# - Escribe otra declaración if que imprima "big place!" si area es mayor que 15.

# Define variables
room = "kit"
area = 14.0

# if statement for room
if room == "kit":
    print("Looking around in the kitchen.")

# if statement for area
if area > 15:
    print("big place!")
