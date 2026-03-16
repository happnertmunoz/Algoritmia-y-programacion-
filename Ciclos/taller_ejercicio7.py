x = 0
y = 0
pasos = 0

while pasos < 10:

    direccion = input("Ingrese dirección (d= derecha, i= izquierda, a= arriba, b= abajo): ")

    if direccion == "d":
        x = x + 1

    elif direccion == "i":
        x = x - 1

    elif direccion == "a":
        y = y + 1

    elif direccion == "b":
        y = y - 1

    pasos = pasos + 1
print("Ubicación final:", x, y)