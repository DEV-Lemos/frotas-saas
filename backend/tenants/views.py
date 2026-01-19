from rest_framework import viewsets

from .models import Empresa, Usuario
from .serializers import EmpresaSerializer, UsuarioSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer


class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.select_related("empresa").all()
    serializer_class = UsuarioSerializer
