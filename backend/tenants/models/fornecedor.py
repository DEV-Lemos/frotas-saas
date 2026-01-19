from django.core.validators import RegexValidator
from django.db import models

from .base import CreatedModel
from .empresa import Empresa


class Fornecedor(CreatedModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="fornecedores")
    nome = models.CharField(max_length=180)

    cnpj = models.CharField(
        max_length=14,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^\d{14}$",
                message="CNPJ deve conter exatamente 14 dígitos (somente números).",
            )
        ],
        help_text="Somente números (14 dígitos).",
    )

    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=180, blank=True)
    tipo = models.CharField(max_length=30, blank=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = "fornecedores"
        verbose_name = "Fornecedor"
        verbose_name_plural = "Fornecedores"
        ordering = ["nome"]

    def __str__(self) -> str:
        return self.nome
