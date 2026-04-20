print("Consumo de energia de los trabajadores.")

trabajadores_kw = {"juan": 100, "pablito" : 110, "Reidy" : 200}
x = input("Ingrese el nombre del trabajador : ").lower()
precio = 0.15

if x in trabajadores_kw:
    consumo = trabajadores_kw[x]
    costo = consumo * precio
    print("consumo : ", consumo, "Kwh")
    print("Total a pagar: $", costo)
else:
    print('El trabajador no existe')