from django.db import models

from apps.core.models import UUIDModel


class Veiculo(UUIDModel):
    STATUS_CHOICES = [
        ("DISPONIVEL", "DISPONIVEL"),
        ("EM_USO", "EM_USO"),
        ("MANUTENCAO", "MANUTENCAO"),
        ("INATIVO", "INATIVO"),
    ]

    empresa = models.ForeignKey("tenants.Empresa", on_delete=models.CASCADE)
    placa = models.CharField(max_length=10)
    renavam = models.CharField(max_length=20, blank=True, null=True)
    chassi = models.CharField(max_length=30, blank=True, null=True)
    marca = models.CharField(max_length=60, blank=True, null=True)
    modelo = models.CharField(max_length=80, blank=True, null=True)
    ano_fabricacao = models.PositiveSmallIntegerField(blank=True, null=True)
    ano_modelo = models.PositiveSmallIntegerField(blank=True, null=True)
    cor = models.CharField(max_length=40, blank=True, null=True)
    tipo = models.CharField(max_length=40, blank=True, null=True)
    combustivel = models.CharField(max_length=30, blank=True, null=True)
    hodometro_km = models.PositiveIntegerField(default=0)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "veiculos"
        constraints = [
            models.UniqueConstraint(
                fields=["empresa", "placa"],
                name="uq_veiculo_empresa_placa",
            )
        ]

    def __str__(self) -> str:
        return self.placa
