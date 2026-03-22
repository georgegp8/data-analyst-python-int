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

# ------------------------------------------------
# Sección 2: Bucle while básico
# ------------------------------------------------
# A continuación puedes ver el ejemplo del vídeo en el que la variable error, inicialmente igual a 50.0,
# se divide por 4 y se imprime en cada ejecución:
#
#   error = 50.0
#   while error > 1 :
#       error = error / 4
#       print(error)
#
# Este ejemplo te resultará útil, porque es hora de que construyas tú mismo un bucle while. Vamos a
# codificar un bucle while que implementa un sistema de control muy básico para un péndulo invertido. Si
# hay una desviación con respecto a la posición perfectamente recta, el bucle while corregirá
# incrementalmente esta desviación.
#
# Ten en cuenta que si el bucle while tarda demasiado en ejecutarse, o tu sesión caduca, puede que
# hayas creado un bucle infinito. En particular, recuerda añadir sangría al contenido del bucle utilizando
# cuatro espacios o la sangría automática, y asegúrate de que las condiciones son las necesarias para que
# el bucle tenga un punto de parada.

# Instrucciones:
# - Crea la variable offset con un valor inicial de 8.
# - Codifica un bucle while que siga ejecutándose mientras offset no sea igual a 0. Dentro del bucle while:
#   - Imprime la frase "correcting...".
#   - A continuación, disminuye en 1 el valor de offset. Puedes hacerlo con offset = offset - 1.
#   - Por último, aún dentro de tu bucle, imprime offset para que puedas ver cómo cambia.

# Initialize offset
offset = 8

# Code the while loop
while offset != 0 :
    print("correcting...")
    offset = offset - 1
    print(offset)

