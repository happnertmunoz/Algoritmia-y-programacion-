# Definición de las funciones solicitadas

def promedio(lista):
    """Calcula la temperatura promedio de la lista."""
    # sum() suma todos los elementos, len() cuenta cuántos elementos hay
    return sum(lista) / len(lista)

def extremos(lista):
    """Encuentra la temperatura más alta y la más baja."""
    # max() encuentra el mayor valor, min() encuentra el menor valor
    return max(lista), min(lista)

def dias_sobre_promedio(lista):
    """Cuenta cuántas veces la temperatura estuvo por encima del promedio."""
    # 1. Primero, obtenemos el promedio usando la función que ya creamos
    prom = promedio(lista)
    
    # 2. Inicializamos un contador en cero
    contador = 0
    
    # 3. Recorremos cada temperatura de la lista con un ciclo
    for temp in lista:
        # Si la temperatura actual es mayor al promedio, sumamos 1 al contador
        if temp > prom:
            contador += 1
            
    return contador

# Programa Principal

# Creamos una lista manual con 24 temperaturas (una por hora) en °C
temperaturas_del_dia = [
    12.0, 12.5, 11.8, 13.5, 13.0, 13.2, # Madrugada (0h - 5h)
    14.0, 15.5, 17.0, 19.5, 21.0, 23.5, # Mañana (6h - 11h)
    25.0, 26.5, 27.0, 26.8, 25.5, 23.0, # Tarde (12h - 17h)
    21.0, 19.5, 18.0, 17.0, 16.0, 15.0  # Noche (18h - 23h)
]

print("\n--- Análisis de Temperaturas del Día ---")

# 1. Calcular e imprimir el promedio
temp_promedio = promedio(temperaturas_del_dia)
# Usamos {:.2f} para que el resultado solo muestre 2 decimales
print(f"1) La temperatura promedio del día fue: {temp_promedio:.2f} °C")

# 2. Determinar e imprimir los extremos
# La función retorna dos valores, así que los guardamos en dos variables
temp_maxima, temp_minima = extremos(temperaturas_del_dia)
print(f"2) La temperatura más alta fue {temp_maxima} °C y la más baja fue {temp_minima} °C")

# 3. Contar e imprimir cuántas veces estuvo sobre el promedio
veces_sobre = dias_sobre_promedio(temperaturas_del_dia)
print(f"3) La temperatura estuvo por encima del promedio {veces_sobre} veces.")