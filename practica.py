import random

productos_disponibles = {
    '1': {'nombre': 'camisetas', 'precio': 20.40,'stock': 40},
    '2': {'nombre': 'pantalones', 'precio': 25.70,'stock': 14},
    '3': {'nombre': 'sudaderas', 'precio': 24.90,'stock': 30},
    '4': {'nombre':'polos','precio':20.0,'stock': 20},
    '5': {'nombre':'abrigos','precio':30.50,'stock': 17},
    '6': {'nombre':'gorras','precio':9.60,'stock': 8},
    '7': {'nombre':'bufandas','precio':10.80,'stock': 5},
    '8': {'nombre':'zapatillas','precio':56.20,'stock': 20},
    '9': {'nombre':'calcetines','precio':2.70,'stock': 30},
    '10': {'nombre':'pijamas','precio':17.80,'stock': 27}
}
tabla_nacionalidades = {
    '1': {'nombre': 'Español', 'iva': 0.21},
    '2': {'nombre': 'Inglés', 'iva': 0.20},
    '3': {'nombre': 'Francés', 'iva': 0.25},
    '4': {'nombre': 'Alemán', 'iva': 0.19},
    '5': {'nombre': 'Italiano', 'iva': 0.22},
    # Agregar más nacionalidades según sea necesario
}

def mostrar_tabla_nacionalidades():
    print("Tabla de Nacionalidades:")
    for key, value in tabla_nacionalidades.items():
        print(f"{key}: {value}")
class Cliente:

    def __init__(self,nombre,apellidos,dni,telefono,dinero_disponible,contrasena,nacionalidad):
        self.listadepedidos=[]
        self.nombre=nombre
        self.apellidos=apellidos
        self.dni=dni
        self.telefono=telefono
        self.dinero=dinero_disponible
        self.contrasena=contrasena
        self.nacionalidad=nacionalidad

    def __str__(self):
        return ("Nombre: "+self.nombre+"\n"
                +"Apellidos: " + self.apellidos+"\n"
                +"el dni es: "+self.dni+"\n"
                +"el telefono es "+str(self.telefono)+"\n"
                +"el dinero disponible es "+str(self.dinero)+"\n"
                +"la contraseña es "+str(self.contrasena)+"\n"
                +"la nacionalidad es : "+self.nacionalidad+"\n")

    def aniadirpedido(self,pedido):
        self.listadepedidos.append(pedido)

    def getDinero(self):
        return self.dinero

    def setDinero(self, nuevoDinero):
        self.dinero=nuevoDinero
class  Producto:
    def __init__(self,precio,nombre):
        self.precio=precio
        self.nombre=nombre

    def __str__(self):
        return("el precio es: " +str(self.precio)+"\n"+
               "el nombre es "+self.nombre+"\n")


class Pedido:
    def __init__(self,cliente,identificador_seguimiento):
        self.productos_eliminados = None
        self.listadeproductos=[]
        self.total=0
        self.cliente=cliente
        self.identificador=identificador_seguimiento

    def get_listadeproductos(self):
        listado = ""
        for p in self.listadeproductos:
            listado = listado + p.nombre + ","

        return listado+"\n"

    def __str__(self):
        return("la lista de productos sera: "+self.get_listadeproductos()+""
               "el total es "+str(self.total)+"\n"
               +"el cliente es "+self.cliente+"\n"
               +"el identificador del producto es "+self.identificador+"\n")

    def setNuevoProducto(self, producto):
        self.listadeproductos.append(producto)
        if productos_disponibles.get(producto.nombre, {}).get('stock', 0) > 0:
            self.listadeproductos.append(producto)
            productos_disponibles[producto.nombre]['stock'] -= 1
            print(f"{producto.nombre} ha sido añadido al carrito por un valor de {producto.precio}.")


    def mostrar_factura(self, producto):
        return True

    def setTotal(self):
        suma = 0
        for p in self.listadeproductos:
            suma = suma + p.precio
        self.total=suma

    def getTotal(self):
        return self.total

    def eliminar_producto(self, nombre_producto):
        for producto in self.listadeproductos:
            if producto.nombre.lower() == nombre_producto.lower():
                self.productos_eliminados.append(producto)
                self.listadeproductos.remove(producto)
                print(f"{nombre_producto} ha sido eliminado del carrito.")
                break


def aplicacion():
    """
    cDavid=Cliente('david','sanchez','leganes','david@gmail.com',66666666,800,1234,'española')
   # print(cDavid)

    producto1=Producto(50,'pera')
    #print(producto1)
    producto2=Producto(20,'manzana')
    #print(producto1)

    pedido1=Pedido(90,'juan','1f2c')
    pedido1.añadir_producto(producto1)
    pedido1.añadir_producto(producto2)

    print(pedido1)
    """

    print('Bienvenido a la aplicacion web')
    print('para crear una cuenta necesitas introducir los siguientes datos y de facturacion: ')


    while True:
        nombre = input('Nombre: ')
        if nombre:
            break
        else:
            print("Por favor, ingresa un nombre válido.")

    while True:
        apellidos = input('Apellidos: ')
        if apellidos:
            break
        else:
            print("Por favor, ingresa apellidos válidos.")

    while True:
        contrasena = input('Contraseña: ')
        if contrasena:
            break
        else:
            print("Por favor, ingresa una contraseña válida.")

    while True:
        dinero = input('Dinero que quieres ingresar: ')
        try:
            dinero = float(dinero)
            break
        except ValueError:
            print("Por favor, ingresa una cantidad de dinero válida.")

    mostrar_tabla_nacionalidades()

    while True:
        nacionalidad = input('Elige el número correspondiente a tu nacionalidad: ')
        if nacionalidad.isdigit() and nacionalidad in tabla_nacionalidades:
            break
        else:
            print("Por favor, ingresa un número válido de la tabla.")

    # Obtener la nacionalidad elegida
    nacionalidad_elegida = tabla_nacionalidades[nacionalidad]
    print(f"Has elegido: {nacionalidad_elegida}")

    while True:
        telefono = input('Teléfono (debe tener 9 digitos): ')
        if telefono.isdigit() and len(telefono) == 9:
            break
        else:
            print("Por favor, ingresa un número de teléfono válido.")

    while True:
        dni = input('DNI (debe tener exactamente 9 caracteres): ')

        # Verificar que el DNI tenga exactamente 9 caracteres
        if len(dni) == 9:
            break
        else:
            print("Error: El DNI debe tener exactamente 9 caracteres. Introduce de nuevo.")

    # Ahora, puedes utilizar la variable 'dni' en tu objeto Cliente o en cualquier otra parte de tu código.

    cliente1=Cliente(nombre,apellidos,dni,telefono,dinero,contrasena,nacionalidad)
    print('¡Usuario registrado correctamente!')
    print(cliente1)
    print('--------------------------------')

    return cliente1

def mostrar_productos():
    print("Productos disponibles para comprar:")
    for clave, valor in productos_disponibles.items():
        print(f"{clave}: {valor['nombre']} - ${valor['precio']}")

        def mostrar_productos():
            print("Productos disponibles para comprar:")
            for clave, valor in productos_disponibles.items():
                print(f"{clave}: {valor['nombre']} - ${valor['precio']}")

def mostrar_menu(cliente):

    identificador_seguimiento=str(random.randint(111111111,999999999))
    pedido1=Pedido(cliente, identificador_seguimiento)

    while True:
        print("\nOpciones:")
        print("1. Comprar")
        print("2. Pagar")
        print("3. Mostrar carrito")
        print("4. Salir")

        opcion = input("Elija una opción (1, 2, 3 o 4): ")

        if opcion == '1':
            mostrar_productos()

            seleccion_usuario = input("Elija el producto por su número: ")

            if seleccion_usuario in productos_disponibles:
                # Obtener información del producto seleccionado
                producto_info = productos_disponibles[seleccion_usuario]
                nombre = producto_info['nombre']
                precio = producto_info['precio']

                # Pedir al usuario la cantidad de unidades que desea comprar
                while True:
                    try:
                        cantidad = int(input(f"¿Cuántas unidades de {nombre} desea comprar? "))
                        if cantidad > 0:
                            break
                        else:
                            print("Por favor, ingrese un número mayor que 0.")
                    except ValueError:
                        print("Por favor, ingrese un número válido.")

                # Verificar si hay suficiente stock antes de añadir el producto al carrito
                stock_disponible = producto_info.get('stock', 0)

                # Asegurarse de que la cantidad solicitada sea menor o igual al stock disponible
                if cantidad <= stock_disponible:
                    for _ in range(cantidad):
                        producto1 = Producto(precio, nombre)
                        pedido1.setNuevoProducto(producto1)
                        productos_disponibles[seleccion_usuario]['stock'] -= 1
                    print(
                        f"{cantidad} unidades de {nombre} han sido añadidas al carrito por un valor total de {precio * cantidad}.")
                    print(f"Stock restante de {nombre}: {stock_disponible - cantidad}.")
                else:
                    print(
                        f"No hay suficiente stock de {nombre} disponible para comprar {cantidad} unidades. Stock actual: {stock_disponible}.")


        elif opcion == '2':
            if not pedido1.listadeproductos:
                print("No hay productos en el carrito. Añade productos antes de pagar.")
            else:
                pedido1.setTotal()
                total_carrito = pedido1.getTotal()
                dinero_en_cuenta = float(cliente.getDinero())

                # Verificar la nacionalidad del cliente
                nacionalidad = cliente.nacionalidad.lower()

                # Obtener la tasa de IVA de la tabla de nacionalidades
                if nacionalidad in tabla_nacionalidades:
                    tasa_iva = tabla_nacionalidades[nacionalidad]['iva']
                else:
                    tasa_iva = 0.0  # Por defecto, si no se encuentra la nacionalidad, se aplica 0% de IVA

                # Calcular el total con la tasa de IVA y redondear a dos decimales
                total_con_iva = round(total_carrito * (1 + tasa_iva), 2)

                if total_con_iva <= dinero_en_cuenta:
                    cliente.setDinero(dinero_en_cuenta - total_con_iva)

                    # Preguntar si se desea recibir la factura por correo
                    desea_factura_por_correo = input("¿Quieres que te enviemos la factura por PDF? (Sí/No): ").lower()

                    if desea_factura_por_correo == 'si':
                        while True:
                            correo_cliente = input("Introduce tu correo para enviar la factura: ")

                            # Verificar que el correo contenga al menos un símbolo "@"
                            if '@' in correo_cliente:
                                # Aquí podrías agregar la lógica para enviar la factura al correo proporcionado
                                print(f"La factura se ha enviado por PDF al correo {correo_cliente}")
                                break
                            else:
                                print(
                                    "Correo no válido. Debe contener al menos un '@'. Introduce el correo nuevamente.")

                    print("¡Compra realizada con éxito!")
                    print(f"Precio total con {tasa_iva * 100}% de IVA: ${total_con_iva}")
                    print(f"Dinero restante en cuenta: ${cliente.getDinero()}")

                    pedido1.listadeproductos = []  # Limpiar el carrito después de la compra
                else:
                    print("No hay suficiente dinero en la cuenta. No se puede realizar la compra.")



        elif opcion == '3':
            if not pedido1.listadeproductos:
                print("Tu carrito está vacío. Añade productos antes de mostrar el carrito.")
            else:
                print("Tu carrito actual contiene los siguientes elementos")
                print(pedido1.get_listadeproductos())
                pedido1.setTotal()  # Calcular el total antes de mostrar el carrito
                print("Total en el carrito: $" + str(pedido1.getTotal()))
                eliminar_producto = input("¿Quieres eliminar un producto del carrito? (Sí/No): ").lower()

                if eliminar_producto == 'si':
                    producto_a_eliminar = input("Ingrese el nombre del producto que desea eliminar: ")
                    for producto in pedido1.listadeproductos:
                        if producto.nombre.lower() == producto_a_eliminar.lower():
                            pedido1.listadeproductos.remove(producto)
                            print(f"{producto_a_eliminar} ha sido eliminado del carrito.")
                            break

        elif opcion == '4':
            print("Gracias por visitarnos. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Por favor, elija 1 para comprar, 2 para pagar, 3 para mostrar, o 4 para salir.")