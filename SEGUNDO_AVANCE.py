productos = productos = [
    {"nombre": "Laptop", "precio": 12000, "cantidad": 20},
    {"nombre": "Mouse", "precio": 250, "cantidad": 50},
    {"nombre": "Teclado", "precio": 800, "cantidad": 30},
    {"nombre": "Monitor", "precio": 2500, "cantidad": 100},
    {"nombre": "Impresora", "precio": 3500, "cantidad": 70}
]

historial = []


def mostrar_menu():
    print("\n===== SISTEMA DE ALMACÉN =====")
    print("1. Agregar producto")
    print("2. Ver productos")
    print("3. Salir")


def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    producto = {"nombre": nombre, "precio": precio,  "cantidad": cantidad, }
    producto.append(producto)
    historial.append(("agregar", producto))

    print("producto agegado")

    productos.append(producto)
    print("Producto agregado correctamente")


def ver_productos():
    if not productos:
        print("No hay productos")
        return

    for p in productos:
        print(p["nombre"], "|", p["precio"], "|", p["cantidad"])


def deshacer():
    if not historial:
        print("No hay acciones para desahacer")
        return
    accion, dato = historial.pop()

    if accion == "Agregar":

        if dato in productos:
            productos.remove(dato)
            print("se deshizo:",  dato[nombre])

        else:
            print("no se pudo  deshacer (No encontrado)")


while True:

    mostrar_menu()
    op = input("opcion:")
    if op == "1":
        agregar_producto()
    elif op == "2":
        ver_productos()
    elif op == "3":
        deshacer()
    elif op == "4":
        break
    else:
        print("Opción inválida")
