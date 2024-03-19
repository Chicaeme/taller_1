#programa para generar un numero aleatorio en Phyton

import random
a = input("Límite inferior:")
b = input("Límite superior:")

a = int(a)
b = int(b)

respuesta = random.randint(a,b)

print(respuesta)