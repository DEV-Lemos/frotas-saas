from django.db import models

from .base import CreatedModel
from .empresa import Empresa
from .fornecedor import Fornecedor
from .veiculo import Veiculo
from .viagem import Viagem


class Despesa(CreatedModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="despesas")
    veiculo = models.ForeignKey(
        Veiculo, on_delete=models.SET_NULL, related_name="despesas", blank=True, null=True
    )
    viagem = models.ForeignKey(
        Viagem, on_delete=models.SET_NULL, related_name="despesas", blank=True, null=True
    )
    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.SET_NULL,
        related_name="despesas",
        blank=True,
        null=True,
    )

    data = models.DateTimeField()
    categoria = models.CharField(max_length=40)
    descricao = models.CharField(max_length=255, blank=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2)

    class Meta:
        db_table = "despesas"
        verbose_name = "Despesa"
        verbose_name_plural = "Despesas"
        ordering = ["-data"]

    def __str__(self) -> str:
        return f"Despesa {self.id}"
