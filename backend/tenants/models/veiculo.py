from django.db import models

from .base import TimestampedModel
from .empresa import Empresa


class Veiculo(TimestampedModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="veiculos")
    placa = models.CharField(max_length=10)
    renavam = models.CharField(max_length=20, blank=True)
    chassi = models.CharField(max_length=30, blank=True)
    marca = models.CharField(max_length=60, blank=True)
    modelo = models.CharField(max_length=80, blank=True)
    ano_fabricacao = models.IntegerField(blank=True, null=True)
    ano_modelo = models.IntegerField(blank=True, null=True)
    cor = models.CharField(max_length=40, blank=True)
    tipo = models.CharField(max_length=40, blank=True)
    combustivel = models.CharField(max_length=30, blank=True)
    hodometro_km = models.IntegerField(default=0)
    status = models.CharField(max_length=20)
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = "veiculos"
        verbose_name = "Veículo"
        verbose_name_plural = "Veículos"
        ordering = ["placa"]
        constraints = [
            models.UniqueConstraint(
                fields=["empresa", "placa"], name="uq_veiculo_empresa_placa"
            )
        ]

    def __str__(self) -> str:
        return self.placa
