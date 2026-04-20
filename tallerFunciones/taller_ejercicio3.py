# Funciones de Gestión de Inventario

def agregar_producto(diccionario, nombre, cantidad, precio):
    """Agrega un nuevo producto o actualiza uno existente."""
    # Verificamos si el producto ya existe en el diccionario
    if nombre in diccionario:
        # Si existe, sumamos la nueva cantidad y actualizamos el precio
        diccionario[nombre]['cantidad'] += cantidad
        diccionario[nombre]['precio'] = precio
        print(f"[+] Producto '{nombre}' actualizado en el inventario.")
    else:
        # Si no existe, creamos un sub-diccionario con sus datos
        diccionario[nombre] = {'cantidad': cantidad, 'precio': precio}
        print(f"[+] Producto '{nombre}' agregado al inventario.")

def eliminar_producto(diccionario, nombre):
    """Elimina un producto del inventario de forma segura."""
    # Primero verificamos si existe para evitar un error del programa
    if nombre in diccionario:
        del diccionario[nombre] # La palabra reservada 'del' borra el elemento
        print(f"[-] Producto '{nombre}' eliminado del inventario.")
    else:
        print(f"[!] Error: El producto '{nombre}' no se encontró.")

def calcular_valor_total(diccionario):
    """Calcula el valor monetario total almacenado en el inventario."""
    total = 0
    # .items() nos permite obtener tanto el nombre(clave) como los datos(valor)
    for nombre, datos in diccionario.items():
        # Multiplicamos la cantidad por el precio de cada producto y lo sumamos
        total += datos['cantidad'] * datos['precio']
    return total

def mostrar_inventario(diccionario):
    """Muestra todos los productos registrados de forma ordenada."""
    print("\n========== INVENTARIO ACTUAL ==========")
    if len(diccionario) == 0:
        print("El inventario está completamente vacío.")
    else:
        for nombre, datos in diccionario.items():
            print(f" {nombre}: {datos['cantidad']} unidades | Precio: ${datos['precio']}")
    print("=======================================\n")

# Programa Principal

# Iniciamos nuestro diccionario principal vacío
mi_inventario = {}

print("--- SISTEMA DE GESTIÓN DE INVENTARIO ---")

# 2. Agregamos productos iniciales
agregar_producto(mi_inventario, "Manzanas", 50, 1.20)
agregar_producto(mi_inventario, "Leche", 20, 2.50)
agregar_producto(mi_inventario, "Peras", 30, 0.80)

# 3. Mostramos cómo quedó el inventario
mostrar_inventario(mi_inventario)

# 4. Actualizamos el inventario (Llegó un nuevo pedido de Manzanas)
agregar_producto(mi_inventario, "Manzanas", 10, 1.25)

# 5. Eliminamos un producto 
eliminar_producto(mi_inventario, "Peras")

# 6. Volvemos a mostrar el inventario tras las modificaciones
mostrar_inventario(mi_inventario)

# 7. Calculamos y mostramos el valor total almacenado
valor_almacenado = calcular_valor_total(mi_inventario)
print(f" El valor total almacenado en el inventario es: ${valor_almacenado:.2f}")