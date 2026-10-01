import datetime 

class ProductoKwikE:
    def __init__(self, descripcion: str, id_producto:int, fecha_vencimiento: datetime.date, precio: float, stock: int, categoria:str):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
        self.categoria = categoria 

    def cambiar_datos(self, descripcion=None, precio=None, stock=None, categoria=None):
        if descripcion is not None:
           self.descripcion = descripcion
        if precio is not None:
           self.precio = precio
        if stock is not None:
           self.stock = stock
        if categoria is not None:
           self.categoria = categoria 

    def calcular_vencimiento_producto(self):
        hoy = datetime.date.today()
        dias_restantes = (self.fecha_vencimiento - hoy).days

        if dias_restantes < 0:
           print("El producto está vencido")
           self.stock = 0

        elif dias_restantes == 0:
           print("El producto vence hoy")

        else:
           print(f"El producto vence en {dias_restantes} dias")

        return dias_restantes 

    def __str__(self) -> str:
        return (f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: $ {self.precio:.2f} | Stock: {self.stock}")


class KwikEMart:
    def __init__(self):
        self.pasillos = {}
        
        self.bebidas = []
        self.snacks = []
        self.conveniencia = []
        self.productos_de_limpieza = []
        self.carnes = []
        self.lacteos = []
        self.productos_de_higiene_personal = []
        self.otros_productos = []

    def agregar_pasillo(self, nombre_pasillo:str):
       if nombre_pasillo not in self.pasillos:
          self.pasillos[nombre_pasillo] = []
          print(f"Pasillo {nombre_pasillo} fue agregado correctamente")

       else:
          print(f"El pasillo {nombre_pasillo} ya existe")

    def agregar_producto_pasillo(self,producto: ProductoKwikE, pasillo:str):
       try:
           if not isinstance(producto, ProductoKwikE):
              raise TypeError("El producto debe pertenecer a la clase ProductoKwikE")
           if pasillo == "Bebidas":
              self.bebidas.append(producto)

           elif pasillo == "Snacks":
              self.snacks.append(producto)

           elif pasillo == "Conveniencia":
              self.conveniencia.append(producto)

           elif pasillo == "Productos de Limpieza":
              self.productos_de_higiene_personal.append(producto)

           elif pasillo == "Carnes":
              self.carnes.append(producto)

           elif pasillo == "Lácteos":
              self.lacteos.append(producto)

           elif pasillo == "Productos de Higiene Personal":
              self.productos_de_higiene_personal.append(producto)

           elif pasillo == "Otros Productos":
              self.otros_productos.append(producto)

           else:
              print("El Pasillo no existe. No se puede agregar el producto")

       except (ValueError, TypeError) as error:
         print("Error:", error)

    def remover_producto_pasillo(self, id_producto:int):
        for pasillo in [self.bebidas, self.snacks, self.conveniencia, self.productos_de_higiene_personal, self.carnes, self.lacteos, self.productos_de_higiene_personal, self.otros_productos]:
           for producto in pasillo:
               if producto.id_producto == id_producto:
                  pasillo.remove(producto)
                  print(f"El producto fue eliminado correctamente")
                  return 
    print(f"Producto no encontrado")
               
    def actualizar_stock_producto(self, id_producto:int, nuevo_stock:int):
        try:
           if nuevo_stock < 0:
              raise ValueError("El stock no puede ser negativo")
           for pasillo in [self.bebidas, self.snacks, self.conveniencia, self.productos_de_higiene_personal, self.carnes, self.lacteos, self.productos_de_higiene_personal, self.otros_productos]:
               for producto in pasillo:
                   if producto.id_producto == id_producto:
                      producto.stock = nuevo_stock
                      print(f"El stock fue actualizado correctamente")
                      return 
           raise ValueError("Producto no encontrado")
        except ValueError as error:
           print("Error:", error)
     

    def calcular_productos_a_vencer_24hs(self):
       hoy = datetime.date.today()
       for pasillo in [self.bebidas, self.snacks, self.conveniencia, self.productos_de_higiene_personal, self.carnes, self.lacteos, self.productos_de_higiene_personal, self.otros_productos]:
          for producto in pasillo [:]:
             dias_restantes = (producto.fecha_vencimiento - hoy).days
             if 0 <= dias_restantes <= 1:
                print(f"El producto {producto.descripcion} está a punto de vencer en {dias_restantes} días")
                pasillo .remove(producto)

    def buscar_producto_por_id(self, id_producto):
       try: 
          if not isinstance(id_producto, int):
             raise TypeError("El ID del producto debe ser un número entero")
          
          for pasillo in [self.bebidas, self.snacks, self.conveniencia, self.productos_de_higiene_personal, self.carnes, self.lacteos, self.productos_de_higiene_personal, self.otros_productos]:
             for producto in pasillo:
                if producto.id_producto == id_producto:
                   return producto
          raise ValueError("No existe un producto con ese ID")
       
       except (TypeError, ValueError) as error:
           print("Error:", error)
           return None  
             