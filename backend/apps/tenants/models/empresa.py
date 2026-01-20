from django.core.validators import RegexValidator
from django.db import models

from apps.core.models import UUIDModel


class Empresa(UUIDModel):
    razao_social = models.CharField(max_length=180)
    nome_fantasia = models.CharField(max_length=180, blank=True, null=True)
    cnpj = models.CharField(
        max_length=14,
        unique=True,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^\d{14}$",
                message="CNPJ deve conter 14 digitos (somente numeros).",
            )
        ],
    )
    email = models.EmailField(max_length=180, blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    ativa = models.BooleanField(default=True)
    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "empresas"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self) -> str:
        return self.nome_fantasia or self.razao_social
