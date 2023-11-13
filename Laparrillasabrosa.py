#-----------------------CLASE USUARIO----------------------------------#
class Usuario:

#CONSTRUCTOR USUARIO / ATRIBUTOS    
    def __init__(self, nombre):
        self.nombre = nombre
        self.carrito = []
        
#MÉTODOS USUARIO

    def comprar_hamburguesa(self, hamburguesa, cantidad):
        self.carrito.append((hamburguesa, cantidad))

    def ver_carrito(self):
        if len(self.carrito) > 0:
            print("\n")
            print("Usted ordenó: ")
            for hamburguesa, cantidad in self.carrito:
                print(f"{hamburguesa} ({cantidad})")
        else:
            print(f"El carrito de {self.nombre} está vacío.")

#-----------------------CLASE ADMINISTRADOR---------------------------#

class Administrador(Usuario):

#CONSTRUCTOR ADMINISTRADOR / ATRIBUTOS     
    def __init__(self, nombre):
        super().__init__(nombre)
        self.administrador = True

#MÉTODOS ADMINISTRADOR
    #def ver_stock(self, tienda):
        #print("Stock disponible:")
        #for numero, hamburguesa in tienda.hamburguesas.items():
            #print(f"{numero}. {hamburguesa.nombre} - Stock: {hamburguesa.stock}")

#-----------------------CLASE HAMBURGUESA---------------------------#
class Hamburguesa:
    
#CONSTRUCTOR HAMBURGUESAS / ATRIBUTOS     
    def __init__(self, nombre, precio, stock_inicial):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock_inicial

#MÉTODOS HAMBURGUESAS
    def comprar(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            return True
        else:
            return False

#---------------------CLASE TIENDA DE HAMBURGUESAS--------------------#
class TiendaHamburguesas:
    
#CONSTRUCTOR TIENDA DE HAMBURGUESAS / ATRIBUTOS (INICIALIZADOS)   
    def __init__(self):
        self.usuarios = {}
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
        }

#MÉTODOS TIENDA DE HAMBURGUESAS
    def agregar_usuario(self, nombre, es_administrador=False):
        if es_administrador:
            usuario = Administrador(nombre)
        else:
            usuario = Usuario(nombre)
        self.usuarios[nombre] = usuario

    def mostrar_menu(self, usuario):
        print("\n")
        print("¡Bienvenido a la Parrilla sabrosa!\n")
        print("Menú:\n")
        for numero, hamburguesa in self.hamburguesas.items():
            print(f"{numero}. {hamburguesa.nombre}: ${hamburguesa.precio}")

    def ver_carrito(self, usuario):
        if usuario in self.usuarios:
            self.usuarios[usuario].ver_carrito()
        else:
            print(f"Usuario {usuario} no encontrado.")

    def comprar_hamburguesa(self, usuario, numero, cantidad):
        if usuario in self.usuarios:
            hamburguesa = self.hamburguesas.get(numero)
            if hamburguesa:
                if hamburguesa.comprar(cantidad):
                    self.usuarios[usuario].comprar_hamburguesa(hamburguesa.nombre, cantidad)
                    print(f"¡Se han agregado {cantidad} {hamburguesa.nombre} al carrito!")
                else:
                    print(f"Lo sentimos, no hay suficiente stock de {hamburguesa.nombre}.")
            else:
                print("El tipo de hamburguesa que eligió no es válido. Por favor, selecciona un número de hamburguesa válido.")
        else:
            print(f"Usuario {usuario} no encontrado.")


#--------------------------------INSTANCIAS------------------------------#

# 1.- Tienda
tienda = TiendaHamburguesas()

# 2.- Agregar usuarios
tienda.agregar_usuario("cliente")
tienda.agregar_usuario("admin", es_administrador=True)

# 3.- Mostrar el menú de hamburguesas (Cliente)
tienda.mostrar_menu("cliente")

# MÉTODO PARA SOLICITAR AL USUARIO

while True:
    try:
        print("\n")
        numero = int(input("Elija la hamburguesa que desea comprar (inserte '0' para concluir su orden): "))
        if numero == 0:
            break
        cantidad = int(input("¿Cuántas hamburguesas desea?: "))
        tienda.comprar_hamburguesa("cliente", numero, cantidad)      
        while True:
            respuesta = input("¿Desea ordenar otra hamburguesa? (S/N): ")
            if respuesta in ["s", "S"]:
                break  # Continuar ordenando
            elif respuesta in ["n", "N"]:
                break  # Finalizar la orden
            else:
                print("Por favor, ingrese 'S' o 'N'.")
        
        if respuesta in ["n", "N"]:
            break  
    except ValueError:
        print("Por favor, ingrese un número válido.")


# 4.- Calcular el total de la compra
total = 0
for hamburguesa, cantidad in tienda.usuarios["cliente"].carrito:
    precio = next(h.precio for n, h in tienda.hamburguesas.items() if h.nombre == hamburguesa)
    total += precio * cantidad

print(f"Total de la compra: ${total}")

