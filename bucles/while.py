# ================================================
# Bucles
# Ejercicios: while
# ================================================

# ------------------------------------------------
# Sección 1: while: calentamiento
# ------------------------------------------------
# El bucle while es como una sentencia if repetida. El código se ejecuta una y otra vez,
# siempre que la condición sea True. Echa otro vistazo a la receta.
#
# while condition :
#     expression
#
# ¿Puedes decir cuántas impresiones hará el siguiente bucle while?

# Instrucciones:
# Ejecuta el siguiente código y cuenta cuántas veces se imprime x:

x = 1
while x < 4 :
    print(x)
    x = x + 1

# ¿Cuántas veces se imprime x?
# a) 0
# b) 1
# c) 2
# d) 3
# e) 4
#
# Respuesta correcta: d) 3
# Explicación: x comienza en 1, y el bucle se ejecuta mientras x < 4:
# - Iteración 1: x=1, imprime 1, x pasa a 2
# - Iteración 2: x=2, imprime 2, x pasa a 3
# - Iteración 3: x=3, imprime 3, x pasa a 4
# - x=4 no cumple x < 4, el bucle termina
