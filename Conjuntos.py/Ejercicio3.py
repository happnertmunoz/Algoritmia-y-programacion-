productos = {
    "manzana": 2.5,
    "banana": 1.8,
    "naranja": 3.0,
    "pera": 2.0,
    "monster": 5.0,
    "agua": 1.0,
    "coca-cola": 3.5}

print("Sistema de inventario")

while True:

    print("1. Verificar producto")
    print("2. Agregar producto")
    print("3. Eliminar producto")
    print("4. Actualizar precio")
    print("5. Ver inventario")
    print("6. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        nombre = input("Ingrese el producto: ").lower()

        if nombre in productos:
            print("El producto existe y cuesta:", productos[nombre])
        else:
            print("El producto no está en el inventario")

    elif opcion == "2":
        nombre = input("Nombre del producto: ").lower()
        unidad = float(input("Cuantas unidades del producto: "))
        if nombre in productos:
           print("Producto agregado")
        else:
            print("El producto no esta en el")

    elif opcion == "3":
        nombre = input("Producto a eliminar: ").lower()

        if nombre in productos:
            del productos[nombre]
            print("Producto eliminado")
        else:
            print("El producto no existe")

    elif opcion == "4":
        nombre = input("Producto a actualizar: ").lower()

        if nombre in productos:
            nuevo_precio = float(input("Nuevo precio: "))
            productos[nombre] = nuevo_precio
            print("Precio actualizado")
        else:
            print("Producto no encontrado")

    elif opcion == "5":
        print("\nInventario:")
        for producto, precio in productos.items():
            print(producto, ":", precio)

    elif opcion == "6":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción inválida")