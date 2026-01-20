from django.db import models

from apps.core.models import UUIDModel


class Manutencao(UUIDModel):
    TIPO_CHOICES = [
        ("PREVENTIVA", "PREVENTIVA"),
        ("CORRETIVA", "CORRETIVA"),
    ]

    STATUS_CHOICES = [
        ("ABERTA", "ABERTA"),
        ("EM_ANDAMENTO", "EM_ANDAMENTO"),
        ("CONCLUIDA", "CONCLUIDA"),
        ("CANCELADA", "CANCELADA"),
    ]

    empresa = models.ForeignKey("tenants.Empresa", on_delete=models.CASCADE)
    veiculo = models.ForeignKey("frota.Veiculo", on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(
        "frota.Fornecedor",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    tipo = models.CharField(max_length=30, choices=TIPO_CHOICES)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    data_prevista = models.DateField(blank=True, null=True)
    data_execucao = models.DateField(blank=True, null=True)
    km_referencia = models.IntegerField(blank=True, null=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "manutencoes"

    def __str__(self) -> str:
        return f"{self.veiculo_id} - {self.tipo}"
