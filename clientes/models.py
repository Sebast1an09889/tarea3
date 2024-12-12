from django.db import models

class Cliente(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=15)
    
    def __str__(self):
        return self.nombre

class Modelo(models.Model):
    
    # Campo para el nombre del modelo
    modelo = models.CharField(
        max_length=255,
        choices=[
            ('Ford Fiesta', 'Ford Fiesta'),
            ('Ferrari', 'Ferrari'),
            ('Lotus', 'Lotus')
        ],
        default='Ford Fiesta'  # Por defecto, se selecciona "Ford Fiesta"
    )
    marca = models.CharField(max_length=255)  # Campo para la marca del vehículo
    año = models.PositiveIntegerField(default=2000)  # Campo para el año del auto
    precio = models.DecimalField(max_digits=10, decimal_places=2)  # Campo para el precio

    def __str__(self):
        #return f"{self.marca} {self.modelo}"
        return self.modelo 

class Auto(models.Model):
    numero_serie = models.CharField(max_length=50, unique=True)
    modelo = models.ForeignKey(Modelo, on_delete=models.CASCADE, related_name='Auto')
    anio = models.PositiveIntegerField()
    color = models.CharField(max_length=30)
    estado = models.CharField(
        max_length=10,
        choices=[('disponible', 'Disponible'), ('vendido', 'Vendido')],
        default='disponible'
    )
    def __str__(self):
        return f"{self.modelo.modelo} ({self.numero_serie})"

class Pedido(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name='pedidos')
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Pedido {self.id} - Cliente: {self.cliente.nombre}"

class DetalleCompra(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='detalles')
    Auto = models.OneToOneField(Auto, on_delete=models.CASCADE, related_name='detalle_compra')
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    descuento = models.DecimalField(max_digits=5, decimal_places=2, default=0.00)

    def __str__(self):
        return f"Detalle {self.id} - Pedido: {self.pedido.id} - Auto: {self.Auto.numero_serie}"