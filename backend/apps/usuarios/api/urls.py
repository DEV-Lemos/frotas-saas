from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.usuarios.api.views import PerfilViewSet, UsuarioPerfilViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r"usuarios", UsuarioViewSet)
router.register(r"perfis", PerfilViewSet)
router.register(r"usuario-perfis", UsuarioPerfilViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
