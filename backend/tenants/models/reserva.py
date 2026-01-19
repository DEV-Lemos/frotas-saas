from django.db import models

from .base import TimestampedModel
from .empresa import Empresa
from .motorista import Motorista
from .usuario import Usuario
from .veiculo import Veiculo


class Reserva(TimestampedModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="reservas")
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE, related_name="reservas")
    motorista = models.ForeignKey(
        Motorista, on_delete=models.SET_NULL, related_name="reservas", blank=True, null=True
    )
    solicitante = models.ForeignKey(
        Usuario, on_delete=models.CASCADE, related_name="reservas"
    )

    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    finalidade = models.CharField(max_length=255, blank=True)
    status = models.CharField(max_length=20)

    class Meta:
        db_table = "reservas"
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        ordering = ["-data_inicio"]

    def __str__(self) -> str:
        return f"Reserva {self.id}"
