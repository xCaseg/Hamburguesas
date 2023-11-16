#-----------------------CLASE Cliente---------------------------#
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []

    def comprar_producto(self, producto, cantidad):
        self.carrito.append((producto, cantidad))


    def ver_carrito(self):
        if len(self.carrito) > 0:
            print("\nUsted ordenó:")
            for producto, cantidad in self.carrito:
                print(f"{producto.nombre} ({cantidad})")
        else:
            print(f"El carrito de {self.nombre} está vacío.")

#-----------------------CLASE PRODUCTO BASE---------------------------#
class ProductoBase:
    def __init__(self, nombre, precio, stock_inicial):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock_inicial

    def comprar(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            return True
        else:
            return False

#-----------------------CLASE HAMBURGUESA---------------------------#
class Hamburguesa(ProductoBase):
    pass

class Bebida(ProductoBase):
    pass

class Papas(ProductoBase):
    pass

#---------------------CLASE TIENDA DE HAMBURGUESAS--------------------#
class Tienda:
    def __init__(self):
        self.cliente = Cliente("Cliente")
        self.hamburguesas = {
            1: Hamburguesa("Hamburguesa Clásica", 65, 100),
            2: Hamburguesa("Hamburguesa de Pollo", 70, 100),
            3: Hamburguesa("Hamburguesa Vegana", 75, 100),
            4: Hamburguesa("Hamburguesa de Pavo", 60, 100),
            5: Hamburguesa("Hamburguesa BBQ", 119, 100),
            6: Hamburguesa("Hamburguesa de sushi", 175, 100),
            7: Hamburguesa("Hamburguesa Mexicana", 155, 100),
            8: Hamburguesa("Hamburguesa Hawaiana", 125, 100),
            9: Hamburguesa("Hamburguesa Ibérica", 100, 100),
            10: Hamburguesa("Hamburguesa Arrachera", 133, 100)
            # ... (otras hamburguesas)
        }

        self.bebidas = {
            1: Bebida("Refresco grande", 60, 100),
            2: Bebida("Refresco mediano", 40, 100),
            3: {"nombre": "Refresco chico", "precio": 25, "stock": 100},
            
            # ... (otras bebidas)
        }

        self.papas = {
           1: Papas("Papas grandes", 60, 100),
           2: Papas("Papas medianas", 40, 100),
           3: {"nombre": "Papas chicas", "precio": 25, "stock": 100},
           # ... (otras papas)
        }

    def mostrar_menu(self):
        print("\n¡Bienvenido a la Parrilla sabrosa!\n")
        print("Menú:\n")
        print("Hamburguesas:\n")
        for numero, hamburguesa in self.hamburguesas.items():
            print(f"{numero}. {hamburguesa.nombre}: ${hamburguesa.precio}")
            
        print("\nBebidas:\n")    
        for numero, bebida in self.bebidas.items():
            if isinstance(bebida, Bebida):
                print(f"{numero}. {bebida.nombre}: ${bebida.precio}")
            elif isinstance(bebida, dict):
                print(f"{numero}. {bebida['nombre']}: ${bebida['precio']}")
                
        print("\nPapas:\n")
        for numero, papa in self.papas.items():
            if isinstance(papa, Papas):
                print(f"{numero}. {papa.nombre}: ${papa.precio}")
            elif isinstance(papa, dict):
                print(f"{numero}. {papa['nombre']}: ${papa['precio']}")

    def comprar_producto(self, categoria, numero, cantidad):
        productos = None
        if categoria == "hamburguesas":
            productos = self.hamburguesas
        elif categoria == "bebidas":
            productos = self.bebidas
        elif categoria == "papas":
            productos = self.papas

        if productos:
            producto = productos.get(numero)
            if producto:
                if isinstance(producto, ProductoBase):
                    if producto.comprar(cantidad):
                        self.cliente.comprar_producto(producto, cantidad)
                        print(f"¡Se han agregado {cantidad} {producto.nombre} al carrito!")
                    else:
                        print(f"Lo sentimos, no hay suficiente stock de {producto.nombre}.")
                elif isinstance(producto, dict):
                    nombre = producto.get('nombre', f"{categoria[:-1]} no válido")
                    if 'precio' in producto:
                        self.cliente.comprar_producto(producto, cantidad)
                        print(f"¡Se han agregado {cantidad} {nombre} al carrito!")
                    else:
                        print(f"{nombre} no tiene un precio definido.")
                else:
                    print(f"El número de {categoria[:-1]} ingresado no es válido. Por favor, seleccione un número válido.")
            else:
                print(f"El número de {categoria[:-1]} ingresado no es válido. Por favor, seleccione un número válido.")
        else:
            print("Categoría de producto no válida.")

# Método para confirmar la compra
def confirmar_compra():
    while True:
        respuesta = input("¿Desea confirmar la compra? (s/n): ").lower()
        if respuesta in ["s", "si"]:
            print(f"\n¡Gracias por su compra, {tienda.cliente.nombre}!")
            break
        elif respuesta in ["n", "no"]:
            print("\nCompra cancelada.")
            break
        else:
            print("Respuesta no válida. Por favor, ingrese 's' para confirmar o 'n' para cancelar.")



# Instanciar la tienda
tienda = Tienda()

# Mostrar el menú
tienda.mostrar_menu()

# Bucle principal para realizar pedidos
while True:
    try:
        print("\n")
        categoria = input("Elija la categoría de producto que desea comprar (hamburguesas/bebidas/papas/0 para concluir la orden): ")

        if categoria == "0":
            break  # Finalizar la orden

        elif categoria in ["hamburguesas", "bebidas", "papas"]:
            numero = int(input(f"Elija el número del producto de {categoria} que desea comprar (inserte '0' para concluir su orden): "))

            if numero == 0:
                break  # Finalizar la orden

            cantidad = int(input("¿Cuántos productos desea?: "))
            tienda.comprar_producto(categoria, numero, cantidad)

        else:
            print("Categoría de producto no válida.")

    except ValueError:
        print("Por favor, ingrese un número válido.")

# Calcular el total de la compra
total = 0
print("\nDetalles de la compra:\n")
for producto, cantidad in tienda.cliente.carrito:
    precio_unitario = producto.precio
    precio_total = precio_unitario * cantidad
    total += precio_total
    print(f"{cantidad} {producto.nombre} x ${precio_unitario} c/u = ${precio_total}")

print(f"\nTotal de la compra: ${total}")

# Confirmar la compra
confirmar_compra()
