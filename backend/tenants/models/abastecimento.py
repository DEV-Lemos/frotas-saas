from django.db import models

from .base import CreatedModel
from .empresa import Empresa
from .fornecedor import Fornecedor
from .veiculo import Veiculo


class Abastecimento(CreatedModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="abastecimentos")
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name="abastecimentos")
    fornecedor = models.ForeignKey(
        Fornecedor,
        on_delete=models.SET_NULL,
        related_name="abastecimentos",
        blank=True,
        null=True,
    )

    data = models.DateTimeField()
    combustivel = models.CharField(max_length=30)
    litros = models.DecimalField(max_digits=10, decimal_places=3)
    valor_total = models.DecimalField(max_digits=12, decimal_places=2)
    km_hodometro = models.IntegerField(blank=True, null=True)
    observacoes = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = "abastecimentos"
        verbose_name = "Abastecimento"
        verbose_name_plural = "Abastecimentos"
        ordering = ["-data"]

    def __str__(self) -> str:
        return f"Abastecimento {self.id}"
