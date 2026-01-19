from django.db import models

from .base import TimestampedModel
from .empresa import Empresa
from .motorista import Motorista
from .reserva import Reserva
from .veiculo import Veiculo


class Viagem(TimestampedModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="viagens")
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name="viagens")
    motorista = models.ForeignKey(
        Motorista, on_delete=models.SET_NULL, related_name="viagens", blank=True, null=True
    )
    reserva = models.ForeignKey(
        Reserva, on_delete=models.SET_NULL, related_name="viagens", blank=True, null=True
    )

    data_saida = models.DateTimeField()
    data_retorno = models.DateTimeField(blank=True, null=True)
    origem = models.CharField(max_length=180, blank=True)
    destino = models.CharField(max_length=180, blank=True)
    km_saida = models.IntegerField(blank=True, null=True)
    km_retorno = models.IntegerField(blank=True, null=True)
    observacoes = models.TextField(blank=True)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "viagens"
        verbose_name = "Viagem"
        verbose_name_plural = "Viagens"
        ordering = ["-data_saida"]

    def __str__(self) -> str:
        return f"Viagem {self.id}"
