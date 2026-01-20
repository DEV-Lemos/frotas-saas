from django.db import models

from apps.core.models import UUIDModel


class Reserva(UUIDModel):
    STATUS_CHOICES = [
        ("SOLICITADA", "SOLICITADA"),
        ("APROVADA", "APROVADA"),
        ("REJEITADA", "REJEITADA"),
        ("CANCELADA", "CANCELADA"),
        ("CONCLUIDA", "CONCLUIDA"),
    ]

    empresa = models.ForeignKey("tenants.Empresa", on_delete=models.CASCADE)
    veiculo = models.ForeignKey("frota.Veiculo", on_delete=models.CASCADE)
    motorista = models.ForeignKey(
        "frota.Motorista",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    solicitante = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    data_inicio = models.DateTimeField()
    data_fim = models.DateTimeField()
    finalidade = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "reservas"

    def __str__(self) -> str:
        return f"{self.veiculo_id} - {self.data_inicio}"
