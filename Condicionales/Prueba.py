while movimientos < 10:
    movimientos += 1
dado = print("Lanza un dado de 4 caras")
caras = input("Que cara cayo? (1, 2, 3, 4): ")
if caras == "1":
    print("Muevase una unidad a la derecha")
elif caras == "2":
    print("Muevase una unidad hacia abajo")
elif caras == "3":
    print("Muevase una unidad a la izquierda")
elif caras == "4":
    print("Muevase una unidad hacia arriba")
movimientos = input("Hizo 10 movimiento? (si/no): ").lower()
if movimientos == "si":
    print("Su posicion final es...")
else: 
    print("Repetir")        