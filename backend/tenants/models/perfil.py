from django.db import models

from .base import BaseUUIDModel
from .empresa import Empresa


class Perfil(BaseUUIDModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="perfis")
    nome = models.CharField(max_length=80)
    descricao = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = "perfis"
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"
        ordering = ["nome"]
        constraints = [
            models.UniqueConstraint(fields=["empresa", "nome"], name="uq_perfil_empresa_nome")
        ]

    def __str__(self) -> str:
        return self.nome
