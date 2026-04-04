productos = []


def mostrar_menu():
    print("\n===== SISTEMA DE ALMACÉN =====")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Salir")


def agregar_producto():
    producto = input("Ingrese el nombre del producto: ")
    productos.append(producto)
    print("Producto agregado correctamente")


def ver_productos():
    if len(productos) == 0:
        print("No hay productos en el almacén")
    else:
        print("\nProductos en almacén:")
        for p in productos:
            print("-", p)


while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        agregar_producto()

    elif opcion == "2":
        ver_productos()

    elif opcion == "3":
        print("Saliendo del sistema...")
        break

    else:
        print("Opción no válida")
