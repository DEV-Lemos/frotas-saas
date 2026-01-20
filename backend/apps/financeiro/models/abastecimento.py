from django.db import models

from apps.core.models import UUIDModel


class Abastecimento(UUIDModel):
    empresa = models.ForeignKey("tenants.Empresa", on_delete=models.CASCADE)
    veiculo = models.ForeignKey("frota.Veiculo", on_delete=models.CASCADE)
    fornecedor = models.ForeignKey(
        "frota.Fornecedor",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    data = models.DateTimeField()
    combustivel = models.CharField(max_length=30)
    litros = models.DecimalField(max_digits=10, decimal_places=3)
    valor_total = models.DecimalField(max_digits=12, decimal_places=2)
    km_hodometro = models.IntegerField(blank=True, null=True)
    observacoes = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "abastecimentos"

    def __str__(self) -> str:
        return f"{self.veiculo_id} - {self.data}"
