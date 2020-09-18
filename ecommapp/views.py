from django.contrib.auth.models import User, Group
from ecommapp.models import cupon, estado_pedido, categoria, pedido, detalle_pedido
from rest_framework import viewsets
from rest_framework import permissions
from ecommapp.serializers import CuponSerializer, Estado_PedidoSerializer, CategoriaSerializer, PedidoSerializer, Detalle_PedidoSerializer
from rest_framework import filters 

class CuponViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = cupon.objects.all()
    serializer_class = CuponSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    #search_fields = ['descripcion']

class Estado_PedidoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = estado_pedido.objects.all()
    serializer_class = Estado_PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    #search_fields = ['descripcion']

class CategoriaViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    #search_fields = ['descripcion']

class PedidoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    #search_fields = ['descripcion']

class Detalle_pedidoViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = detalle_pedido.objects.all()
    serializer_class = Detalle_PedidoSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    #search_fields = ['descripcion']