productos = productos = [
    {"nombre": "manzana", "precio": 10.0, "cantidad": 5},
    {"nombre": "leche", "precio": 22.5, "cantidad": 10},
    {"nombre": "pan", "precio": 8.0, "cantidad": 15},
    {"nombre": "huevo", "precio": 30.0, "cantidad": 12},
    {"nombre": "arroz", "precio": 18.0, "cantidad": 20}
]


def mostrar_menu():
    print("\n===== SISTEMA DE ALMACÉN =====")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Salir")


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    productos.append(producto)
    print("Producto agregado correctamente")


def ver_productos():
    if len(productos) == 0:
        print("No hay productos en el almacén")
    else:
        print("\nProductos en almacén:")
        for p in productos:
            print("------------------")
            print("Nombre:", p["nombre"])
            print("Precio:", p["precio"])
            print("Cantidad:", p["cantidad"])


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
