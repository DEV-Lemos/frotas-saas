from django.db import models

from apps.core.models import UUIDModel


class Despesa(UUIDModel):
    CATEGORIA_CHOICES = [
        ("PEDAGIO", "PEDAGIO"),
        ("ESTACIONAMENTO", "ESTACIONAMENTO"),
        ("MULTA", "MULTA"),
        ("SEGURO", "SEGURO"),
        ("OUTROS", "OUTROS"),
    ]

    empresa = models.ForeignKey("tenants.Empresa", on_delete=models.CASCADE)
    veiculo = models.ForeignKey(
        "frota.Veiculo",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    viagem = models.ForeignKey(
        "operacao.Viagem",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    fornecedor = models.ForeignKey(
        "frota.Fornecedor",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    data = models.DateTimeField()
    categoria = models.CharField(max_length=40, choices=CATEGORIA_CHOICES)
    descricao = models.CharField(max_length=255, blank=True, null=True)
    valor = models.DecimalField(max_digits=12, decimal_places=2)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "despesas"

    def __str__(self) -> str:
        return f"{self.categoria} - {self.valor}"
