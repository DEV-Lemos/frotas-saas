from django.db import models

from apps.core.models.base import UUIDModel


class Empresa(UUIDModel):
    razao_social = models.CharField(max_length=180)
    nome_fantasia = models.CharField(max_length=180, null=True, blank=True)

    cnpj = models.CharField(
        max_length=14,
        unique=True,
        null=True,
        blank=True,
        help_text="Somente números",
    )

    email = models.EmailField(max_length=180, null=True, blank=True)
    telefone = models.CharField(max_length=20, null=True, blank=True)

    ativa = models.BooleanField(default=True)

    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        db_table = "empresas"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self) -> str:
        return self.nome_fantasia or self.razao_social
