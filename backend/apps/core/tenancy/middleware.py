from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin

from .context import get_empresa_from_header


class TenantMiddleware(MiddlewareMixin):
    """
    Injeta request.empresa para todo o ciclo da request.

    Para MVP: exige header em rotas autenticadas.
    Você pode flexibilizar (ex.: permitir rotas públicas sem empresa).
    """

    def process_request(self, request):
        # Exemplo: se você tiver rotas públicas, pode "liberar" aqui por path.
        # if request.path.startswith("/health/"):
        #     return None

        empresa = get_empresa_from_header(request)
        request.empresa = empresa  # padrão útil

        # Se você quer OBRIGAR tenant em tudo:
        if request.user.is_authenticated and empresa is None:
            return JsonResponse(
                {"detail": "Tenant ausente ou inválido. Envie o header X-Empresa-Id."},
                status=400,
            )

        return None
