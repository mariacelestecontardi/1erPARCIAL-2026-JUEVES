import datetime 

class ProductoKwikE:
    def __init__(self, descripcion: str, id_producto:int, fecha_vencimiento: date, precio: float, stock: int, categoria:str):
        self.descripcion = descripcion
        self.id_producto = id_producto
        self.fecha_vencimiento = fecha_vencimiento
        self.precio = precio
        self.stock = stock
        self.categoria = categoria 

    def __str__(self):
        return f"Producto: {self.descripcion} | ID: {self.id_producto} | Precio: ${self.precio:.2f} | Stock: {self.stock}"

    def __eq__(self, otro):
        return (self.id_producto == otro.id_producto and self.descripcion == otro.descripcion)
            
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

producto1 = ProductoKwikE("Alfajor Rasta Chocolate Negro", 66, datetime.date(2026, 12, 12), 3000.0, 10, "Golosinas")
producto1.calcular_vencimiento_producto()
