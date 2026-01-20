from django.db import models

from apps.core.models import UUIDModel


class Fornecedor(UUIDModel):
    empresa = models.ForeignKey("tenants.Empresa", on_delete=models.CASCADE)
    nome = models.CharField(max_length=180)
    cnpj = models.CharField(max_length=14, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=180, blank=True, null=True)
    tipo = models.CharField(max_length=30, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "fornecedores"

    def __str__(self) -> str:
        return self.nome
