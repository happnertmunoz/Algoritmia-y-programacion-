hora = input("La hora son las 6 (si/no) :").lower()
if hora == "si" :
   boton = input("¿Presionó el botón de apagado? (si/no): ").lower()
   if boton == "si" :
      print("Se apago la alarma")
   else:
     print("La alarma suena 1 minuto")
     print("Se apaga despues")
else:
   print("No es hora de la arma")