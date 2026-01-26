from rest_framework import permissions, viewsets

from apps.tenants.models import Empresa

from .serializers import EmpresaSerializer


class EmpresaViewSet(viewsets.ModelViewSet):
    """
    CRUD for tenant companies.
    In production, this is usually restricted to internal admins.
    """

    serializer_class = EmpresaSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Empresa.objects.all().order_by("-criada_em")
