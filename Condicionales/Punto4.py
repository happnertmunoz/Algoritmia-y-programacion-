tanque_vacio = input("Detector de tanque vacio activado? (si/no) : ").lower()
if tanque_vacio == "si" :
    print("Valvula abierta")
else:
    tanque_lleno = input("Detector de tanque lleno activado? (si/no): ").lower()
     
    if tanque_lleno == "si" :
        print("Cerrar valvula")
    else:
        print("Abrir valvula")