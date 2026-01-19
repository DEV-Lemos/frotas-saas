from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import EmpresaViewSet, UsuarioViewSet

router = DefaultRouter()
router.register("empresas", EmpresaViewSet, basename="empresa")
router.register("usuarios", UsuarioViewSet, basename="usuario")

urlpatterns = [
    path("", include(router.urls)),
]
