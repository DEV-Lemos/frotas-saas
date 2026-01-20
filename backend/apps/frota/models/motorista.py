from django.core.validators import RegexValidator
from django.db import models

from apps.core.models import UUIDModel


class Motorista(UUIDModel):
    empresa = models.ForeignKey("tenants.Empresa", on_delete=models.CASCADE)
    nome = models.CharField(max_length=180)
    cpf = models.CharField(
        max_length=11,
        blank=True,
        null=True,
        validators=[
            RegexValidator(
                regex=r"^\d{11}$",
                message="CPF deve conter 11 digitos (somente numeros).",
            )
        ],
    )
    cnh_numero = models.CharField(max_length=30, blank=True, null=True)
    cnh_categoria = models.CharField(max_length=5, blank=True, null=True)
    cnh_validade = models.DateField(blank=True, null=True)
    telefone = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(max_length=180, blank=True, null=True)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "motoristas"
        constraints = [
            models.UniqueConstraint(
                fields=["empresa", "cpf"],
                name="uq_motorista_empresa_cpf",
            )
        ]

    def __str__(self) -> str:
        return self.nome
