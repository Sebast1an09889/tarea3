from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ClienteViewSet, ModeloViewSet, AutoViewSet, PedidoViewSet, DetalleCompraViewSet
from . import views
from .views import cuenta_view, compra_view
from .views import exportar_todo_csv
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

#from rest_framework_simplejwt import (
#    TokenObtainPairView,
#    TokenRefreshView,
#)


router = DefaultRouter()
router.register('clientes', ClienteViewSet)
router.register('modelo', ModeloViewSet)
router.register('Auto', AutoViewSet)
router.register('pedidos', PedidoViewSet)
router.register('detalles_compra', DetalleCompraViewSet)

urlpatterns = [
    # url para la API REST
    path('api/', include(router.urls)),
    
    #Ruta de vista Compra, Cuenta
    path('Cuenta/', cuenta_view, name='cuenta'),
    path('Compra/', compra_view, name='compra'),
    
    #Ruta para exportar datos en CsV
    path('exportar_todo/', exportar_todo_csv, name='exportar_todo'),
    
    #Rutas de Token 
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    #rutas de pis 
    #path('api/clientes/', ClienteViewSet.as_view({'get': 'list'}), name='api_clientes'),
    #path('api/modelos/', ModeloViewSet.as_view({'get': 'list'}), name='api_modelos'),
    #path('api/autos/', AutoViewSet.as_view({'get': 'list'}), name='api_autos'),
    #path('api/pedidos/', PedidoViewSet.as_view({'get': 'list'}), name='api_pedidos'),
    #path('api/detallecompra/', DetalleCompraViewSet.as_view({'get': 'list'}), name='api_detallecompra'),
]
