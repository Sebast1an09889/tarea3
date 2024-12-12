from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import Cliente, Modelo, Auto, Pedido, DetalleCompra
from .serializer import ClienteSerializer, ModeloSerializer, AutoSerializer, PedidoSerializer, DetalleCompraSerializer
from .filters import ClienteFilter, AutoFilter

# Importaciones necesarias para la exportación en CSV
import csv
from django.http import HttpResponse
from django.shortcuts import render

# Vista para exportar datos completos a un archivo CSV
def exportar_todo_csv(request):
    
    #Vista para generar un archivo CSV con todos los datos relacionados:Clientes, Pedidos, Detalles de Compra, y Autos.
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="datos_completos.csv"'

    # Escribir encabezados al archivo CSV
    writer = csv.writer(response)
    writer.writerow(['Cliente', 'Correo', 'Teléfono', 'Pedido ID', 'Fecha', 'Auto', 'Modelo', 'Color', 'Estado', 'Precio', 'Descuento'])

    # Obtener datos relacionados
    clientes = Cliente.objects.all()
    for cliente in clientes:
        pedidos = cliente.pedidos.all()
        for pedido in pedidos:
            detalles = pedido.detalles.all()
            for detalle in detalles:
                writer.writerow([
                    cliente.nombre,
                    cliente.correo,
                    cliente.telefono,
                    pedido.id,
                    pedido.fecha,
                    detalle.auto.numero_serie,
                    detalle.auto.modelo.modelo,
                    detalle.auto.color,
                    detalle.auto.estado,
                    detalle.precio,
                    detalle.descuento,
                ])

    return response

# Vista para exportar clientes filtrados
def exportar_clientes(request):
    
    #Exporta una lista de clientes a un archivo CSV basado en un filtro opcional por nombre.
    nombre_filtro = request.GET.get('nombre', '')
    clientes = Cliente.objects.filter(nombre__icontains=nombre_filtro)

    # Crear la respuesta CSV
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="clientes.csv"'

    writer = csv.writer(response)
    writer.writerow(['ID', 'Nombre', 'Email'])

    for cliente in clientes:
        writer.writerow([cliente.id, cliente.nombre, cliente.correo])

    return response

# Vistas relacionadas con las plantillas HTML
def cuenta_view(request):
    #Renderiza la plantilla Cuenta.html con la lista de clientes.
    clientes = Cliente.objects.all()  # Obtener todos los clientes registrados
    return render(request, 'Cuenta.html', {'clientes': clientes})

def compra_view(request):
    #Renderiza la plantilla Compra.html con datos de autos disponibles.
    autos = Auto.objects.filter(estado='disponible')  # Mostrar solo autos disponibles
    return render(request, 'compra.html', {'autos': autos})

# ViewSets para la API
class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['nombre', 'correo']

class ModeloViewSet(viewsets.ModelViewSet):
    queryset = Modelo.objects.all()
    serializer_class = ModeloSerializer

class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer
    filter_backends = [DjangoFilterBackend]
    # filterset_class = AutoFilter
    filterset_fields = ['modelo__modelo', 'color', 'estado']

class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer

class DetalleCompraViewSet(viewsets.ModelViewSet):
    queryset = DetalleCompra.objects.all()
    serializer_class = DetalleCompraSerializer
