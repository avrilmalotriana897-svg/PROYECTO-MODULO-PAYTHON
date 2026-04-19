productos = [
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
    print("3. Deshacer última acción")
    print("4. Salir")


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
    historial.append(("agregar", producto))

    print("✅ Producto agregado correctamente")


def ver_productos():
    if not productos:
        print("No hay productos")
        return

    print("\n--- LISTA DE PRODUCTOS ---")
    for p in productos:
        print(p["nombre"], "|", p["precio"], "|", p["cantidad"])


def deshacer():
    if not historial:
        print("No hay acciones para deshacer")
        return

    accion, dato = historial.pop()

    if accion == "agregar":
        if dato in productos:
            productos.remove(dato)
            print("↩️ Se deshizo:", dato["nombre"])
        else:
            print("No se pudo deshacer (no encontrado)")


while True:
    mostrar_menu()
    op = input("Opción: ")

    if op == "1":
        agregar_producto()
    elif op == "2":
        ver_productos()
    elif op == "3":
        deshacer()
    elif op == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción inválida")
