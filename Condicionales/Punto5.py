luz_rojo = input("Se enciende la luz Roja (si/no) : ").lower()
if luz_rojo == "si":
    print("Se enciende por 20 segundos")
    print("Apagar luz Roja")
else:
    print("Error en la luz Roja") 
    exit()   
luz_verde = input("Endender luz verde? (si/no) : ").lower()
if luz_verde == "si":
    print("Encendida por 40 segundos")
else:
    print("Error en la luz verde")
    exit()
luz_amarilla = input("Endender luz amarilla junto a la verde? (si/no) : ").lower()
if luz_amarilla == "si":
    print("Encendida por 5 segundos")
else:
    print("Error en la luz Amarilla")
    exit()    
ciclo = input("Apagar las luces verde y amarilla? (si/no) : ").lower()
if ciclo == "si":
    print("Repetir el ciclo")
else:
    print("Error en el ciclo")
    exit()       