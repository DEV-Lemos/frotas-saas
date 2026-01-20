from django.urls import include, path
from rest_framework.routers import DefaultRouter

from apps.tenants.api.views import EmpresaViewSet

router = DefaultRouter()
router.register(r"empresas", EmpresaViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
