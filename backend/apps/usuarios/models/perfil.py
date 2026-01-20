from django.db import models

from apps.core.models import UUIDModel


class Perfil(UUIDModel):
    empresa = models.ForeignKey("tenants.Empresa", on_delete=models.CASCADE)
    nome = models.CharField(max_length=80)
    descricao = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        db_table = "perfis"
        constraints = [
            models.UniqueConstraint(
                fields=["empresa", "nome"],
                name="uq_perfil_empresa_nome",
            )
        ]

    def __str__(self) -> str:
        return self.nome
