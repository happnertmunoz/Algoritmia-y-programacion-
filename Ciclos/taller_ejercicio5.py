vacio = input("El tanque esta vacio (si/no): ")
lleno = "no"
valvula = "cerrada"

while vacio == "si":
    print("Tanque vacio / abriendo valvula")
    valvula = "abierta"

    lleno = input("El tanque esta lleno? (si/no): ")
    if lleno == "si":
        valvula = "cerrada"
        print("Tanque lleno / cerrando valvula")
        break