from django.db import models

from .base import TimestampedModel
from .empresa import Empresa
from .fornecedor import Fornecedor
from .veiculo import Veiculo


class Manutencao(TimestampedModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="manutencoes")
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name="manutencoes")
    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.SET_NULL,
        related_name="manutencoes",
        blank=True,
        null=True,
    )

    tipo = models.CharField(max_length=30)
    descricao = models.CharField(max_length=255, blank=True)
    data_prevista = models.DateField(blank=True, null=True)
    data_execucao = models.DateField(blank=True, null=True)
    km_referencia = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "manutencoes"
        verbose_name = "Manutenção"
        verbose_name_plural = "Manutenções"
        ordering = ["-data_prevista"]

    def __str__(self) -> str:
        return f"Manutenção {self.id}"
