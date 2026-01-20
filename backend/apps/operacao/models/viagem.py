from django.db import models

from apps.core.models import UUIDModel


class Viagem(UUIDModel):
    STATUS_CHOICES = [
        ("ABERTA", "ABERTA"),
        ("FINALIZADA", "FINALIZADA"),
        ("CANCELADA", "CANCELADA"),
    ]

    empresa = models.ForeignKey("tenants.Empresa", on_delete=models.CASCADE)
    veiculo = models.ForeignKey("frota.Veiculo", on_delete=models.CASCADE)
    motorista = models.ForeignKey(
        "frota.Motorista",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    reserva = models.ForeignKey(
        "operacao.Reserva",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    data_saida = models.DateTimeField()
    data_retorno = models.DateTimeField(blank=True, null=True)
    origem = models.CharField(max_length=180, blank=True, null=True)
    destino = models.CharField(max_length=180, blank=True, null=True)
    km_saida = models.IntegerField(blank=True, null=True)
    km_retorno = models.IntegerField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "viagens"

    def __str__(self) -> str:
        return f"{self.veiculo_id} - {self.data_saida}"
