from django.db import models

from apps.core.models import UUIDModel


class Anexo(UUIDModel):
    empresa = models.ForeignKey("tenants.Empresa", on_delete=models.CASCADE)
    entidade = models.CharField(max_length=40)
    entidade_id = models.UUIDField()
    nome_arquivo = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=100, blank=True, null=True)
    url_armazenamento = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "anexos"

    def __str__(self) -> str:
        return self.nome_arquivo
