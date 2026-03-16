hora = int(input("Ingrese la hora (0-23): "))
if hora == 6:
    print("Alarma encendida")
    segundos = 0 
    boton = "no"

    while segundos < 60 and boton != "si":
        print("Sonando alarma...")
        boton = input("Presiono el boton de apagado? (si/no): ")
        segundos = segundos + 1 
    print("Alarma apagada")

else:
    print("No es hora de alarma")