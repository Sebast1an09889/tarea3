from django_filters import rest_framework as filters
from .models import Cliente, Auto
# funcion de orden superior (programacion )
#verifica que los elementos hagan una determinada condicion
#un objeto  iterable con elemtos que cumplen la funcion
class ClienteFilter(filters.FilterSet):
    nombre = filters.CharFilter(lookup_expr='icontains')  # Búsqueda insensible a mayúsculas
    correo = filters.CharFilter(lookup_expr='icontains')  # Búsqueda parcial

    class Meta:
        model = Cliente
        fields = ['nombre', 'correo']

class AutoFilter(filters.FilterSet):
    #modelo = filters.CharFilter(field_name='modelo__modelo', lookup_expr='icontains')
    modelo = filters.CharFilter(field_name='modelo__modelo', lookup_expr='icontains')
    color = filters.CharFilter(lookup_expr='icontains')
    estado = filters.ChoiceFilter(choices=[('disponible', 'Disponible'), ('vendido', 'Vendido')])

    class Meta:
        model = Auto
        fields = {'modelo':['exact'],
                'color':['icontains'],
                'estado':['exact'],
                    }
