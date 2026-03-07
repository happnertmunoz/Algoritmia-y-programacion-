sistemas_de_votaciones = print("Candidatos disponibles: A, M, N")
opcion = input("Elige un candidato: ").upper()
if opcion == "A":
    print("Usted ha votado por el partido Amarillo")
elif opcion == "M":
    print("Usted ha votado por el partido Morado")
elif opcion == "N":
    print("Usted ha votado poe el partido Naranja")
else:
    print("Opcion erronea")            