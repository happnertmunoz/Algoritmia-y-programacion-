import random # Importamos la librería nativa para generar cosas aleatorias

# Funciones del Juego

def elegir_dificultad():
    """1) Pide al usuario que elija la dificultad y retorna la cantidad de intentos."""
    print("Niveles de dificultad:")
    print("1. Fácil (10 intentos)")
    print("2. Medio (7 intentos)")
    print("3. Difícil (5 intentos)")
    
    # Usamos un ciclo infinito que solo se rompe si el usuario elige bien
    while True:
        opcion = input("Elige el nivel (1, 2 o 3): ")
        if opcion == '1':
            return 10
        elif opcion == '2':
            return 7
        elif opcion == '3':
            return 5
        else:
            print("[!] Opción inválida. Por favor ingresa 1, 2 o 3.")

def generar_numero():
    """2) Genera y retorna un número aleatorio entre 1 y 100."""
    # randint incluye tanto el 1 como el 100 en las posibilidades
    return random.randint(1, 100)

def guardar_historial(mensaje):
    """Bonus: Guarda el resultado en un archivo de texto (.txt)."""
    # La letra 'a' significa 'append' (añadir al final sin borrar lo anterior)
    with open("historial_juego.txt", "a", encoding="utf-8") as archivo:
        archivo.write(mensaje + "\n")

def jugar(intentos):
    """3 y 4) Lógica principal: pistas y conteo de intentos."""
    numero_secreto = generar_numero()
    intentos_iniciales = intentos # Guardamos este dato para el historial
    
    print(f"\n¡He pensado en un número entre 1 y 100!")
    print(f"Tienes {intentos} intentos para adivinarlo. ¡Suerte!")
    
    while intentos > 0:
        print(f"\nTe quedan {intentos} intentos.")
        
        # try-except evita que el juego se cierre si el usuario escribe letras
        try:
            adivinanza = int(input("Ingresa tu número: "))
        except ValueError:
            print("[!] Error:¡Debes ingresar un número entero!")
            continue # Vuelve al inicio del ciclo sin restar intentos
            
        # Comparamos el número ingresado con el secreto
        if adivinanza == numero_secreto:
            mensaje = f"VICTORIA: Adivinó el {numero_secreto} (Nivel: {intentos_iniciales} intentos)."
            print(f"\n¡Felicidades! ¡Has adivinado el número secreto {numero_secreto}!")
            guardar_historial(mensaje)
            return # Termina la función (y por ende, el juego)
            
        elif adivinanza < numero_secreto:
            print("Pista: El número secreto es MAYOR")
        else:
            print("Pista: El número secreto es MENOR")
            
        intentos -= 1 # Restamos un intento por cada fallo
        
    # Si el ciclo while termina (llega a 0) y no retornó victoria, el jugador perdió
    mensaje = f"DERROTA: No adivinó el {numero_secreto} (Nivel: {intentos_iniciales} intentos)."
    print(f"¡Juego terminado! Te has quedado sin intentos.")
    print(f"El número secreto era: {numero_secreto}")
    guardar_historial(mensaje)

# Programa Principal

print("--- JUEGO DE ADIVINAR EL NÚMERO ---")
# 1. Llamamos a la función de dificultad y guardamos los intentos
intentos_asignados = elegir_dificultad()

# 2. Le pasamos esos intentos a la función que arranca el juego
jugar(intentos_asignados)

print("\n(Se ha actualizado el archivo 'historial_juego.txt' con tu resultado)")