# Base de datos de la máquina (Diccionario)
# Las claves son los nombres y los valores son los precios
inventario_maquina = {
    "Papas": 2500.0,
    "Gaseosa": 3000.0,
    "Chocolatina": 1500.0,
    "Galletas": 1200.0,
    "Agua": 2000.0
}

# Funciones de la Máquina Dispensadora

def verificar_pago_insuficiente(precio, dinero_ingresado):
    """Bonus: Verifica e indica si el valor es menor al solicitado."""
    if dinero_ingresado < precio:
        faltante = precio - dinero_ingresado
        print(f"[!] Error: Dinero insuficiente. Te faltan ${faltante:.2f} para completar la compra.")
        # Retornamos True para avisarle al programa que hubo un problema
        return True 
    # Retornamos False indicando que no faltó dinero (todo está bien)
    return False

def procesar_compra(diccionario, producto, dinero_ingresado):
    """3 y 4) Verifica la devuelta y muestra los mensajes correspondientes."""
    precio = diccionario[producto]
    
    # Llamamos a nuestra función del Bonus
    es_insuficiente = verificar_pago_insuficiente(precio, dinero_ingresado)
    
    # Si la función del Bonus nos dijo que falta dinero, cancelamos la compra
    if es_insuficiente:
        print("=> Compra cancelada. Devolviendo tu dinero...")
        return # Termina la función aquí mismo
        
    # Si pasamos la validación anterior, calculamos la devuelta
    devuelta = dinero_ingresado - precio
    
    print(f"Dispensando producto: {producto}")
    
    if devuelta > 0:
        print(f"Toma tu devuelta: ${devuelta:.2f}")
    else:
        print("Pago exacto. No hay devuelta.")

# Programa Principal 

print("--- MÁQUINA DISPENSADORA ---")
print("Productos disponibles hoy:")
for prod, prec in inventario_maquina.items():
    print(f"  - {prod}: ${prec:.2f}")

# 2) Leemos lo que el usuario ingresa
# .capitalize() convierte la primera letra en mayúscula (ej. si escribe "agua" pasa a "Agua")
producto_elegido = input("\nEscribe el nombre del producto que deseas: ").capitalize()

# Validamos que el producto exista en nuestro diccionario
if producto_elegido in inventario_maquina:
    precio_actual = inventario_maquina[producto_elegido]
    print(f"Has seleccionado {producto_elegido}. Total a pagar: ${precio_actual:.2f}")
    
    # Usamos try-except para evitar que el programa falle si escriben letras en vez de números
    try:
        pago = float(input("Ingresa la cantidad de dinero con la que vas a pagar: $"))
        # Llamamos a la función que hace toda la magia
        procesar_compra(inventario_maquina, producto_elegido, pago)
    except ValueError:
        print("[!] Error: Debes ingresar un valor numérico válido para pagar.")
else:
    print("[!] Lo sentimos, ese producto no existe en esta máquina.")