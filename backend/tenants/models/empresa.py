from django.core.validators import RegexValidator
from django.db import models

from .base import TimestampedModel


class Empresa(TimestampedModel):
    razao_social = models.CharField(max_length=180)
    nome_fantasia = models.CharField(max_length=180, blank=True)

    cnpj = models.CharField(
        max_length=14,
        blank=True,
        null=True,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^\d{14}$",
                message="CNPJ deve conter exatamente 14 dígitos (somente números).",
            )
        ],
        help_text="Somente números (14 dígitos).",
    )

    email = models.EmailField(max_length=180, blank=True)
    telefone = models.CharField(max_length=20, blank=True)

    ativa = models.BooleanField(default=True)

    class Meta:
        db_table = "empresas"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["razao_social"]

    def __str__(self) -> str:
        return self.nome_fantasia or self.razao_social
