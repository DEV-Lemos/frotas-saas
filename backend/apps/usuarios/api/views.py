from rest_framework import permissions, viewsets
from rest_framework.exceptions import ValidationError

from apps.usuarios.models import Perfil, Usuario, UsuarioPerfil

from .serializers import PerfilSerializer, UsuarioPerfilSerializer, UsuarioSerializer


def _get_empresa_or_error(request):
    empresa = getattr(request, "empresa", None)
    if empresa is None:
        raise ValidationError({"detail": "Empresa nao informada. Envie o header X-Empresa-Id."})
    return empresa


class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Usuario.objects.select_related("empresa").all().order_by("-criado_em")

    def get_queryset(self):
        empresa = getattr(self.request, "empresa", None)
        if empresa is None:
            return Usuario.objects.none()
        return self.queryset.filter(empresa=empresa)

    def perform_create(self, serializer):
        empresa = _get_empresa_or_error(self.request)
        serializer.save(empresa=empresa)


class PerfilViewSet(viewsets.ModelViewSet):
    serializer_class = PerfilSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = Perfil.objects.select_related("empresa").all().order_by("nome")

    def get_queryset(self):
        empresa = getattr(self.request, "empresa", None)
        if empresa is None:
            return Perfil.objects.none()
        return self.queryset.filter(empresa=empresa)

    def perform_create(self, serializer):
        empresa = _get_empresa_or_error(self.request)
        serializer.save(empresa=empresa)


class UsuarioPerfilViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioPerfilSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = (
        UsuarioPerfil.objects.select_related("usuario", "perfil").all().order_by("-criado_em")
    )

    def get_queryset(self):
        empresa = getattr(self.request, "empresa", None)
        if empresa is None:
            return UsuarioPerfil.objects.none()
        return self.queryset.filter(usuario__empresa=empresa)

    def perform_create(self, serializer):
        _get_empresa_or_error(self.request)
        serializer.save()
