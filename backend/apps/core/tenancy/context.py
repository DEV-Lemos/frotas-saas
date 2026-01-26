from uuid import UUID

from django.http import HttpRequest

from apps.tenants.models import Empresa

TENANT_HEADER = "HTTP_X_EMPRESA_ID"  # Django transforma "X-Empresa-Id" nisso


def get_empresa_from_header(request: HttpRequest) -> Empresa | None:
    raw = request.META.get(TENANT_HEADER)
    if not raw:
        return None

    try:
        empresa_id = UUID(raw)
    except ValueError:
        return None

    try:
        return Empresa.objects.get(id=empresa_id, ativa=True)
    except Empresa.DoesNotExist:
        return None
