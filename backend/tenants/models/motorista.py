from django.core.validators import RegexValidator
from django.db import models

from .base import TimestampedModel
from .empresa import Empresa


class Motorista(TimestampedModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="motoristas")
    nome = models.CharField(max_length=180)

    cpf = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^\d{11}$",
                message="CPF deve conter exatamente 11 dígitos (somente números).",
            )
        ],
        help_text="Somente números (11 dígitos).",
    )

    cnh_numero = models.CharField(max_length=30, blank=True)
    cnh_categoria = models.CharField(max_length=5, blank=True)
    cnh_validade = models.DateField(blank=True, null=True)

    telefone = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=180, blank=True)

    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = "motoristas"
        verbose_name = "Motorista"
        verbose_name_plural = "Motoristas"
        ordering = ["nome"]
        constraints = [
            models.UniqueConstraint(
                fields=["empresa", "cpf"], name="uq_motorista_empresa_cpf"
            )
        ]

    def __str__(self) -> str:
        return self.nome
