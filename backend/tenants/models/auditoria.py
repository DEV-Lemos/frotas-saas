from django.db import models

from .base import CreatedModel
from .empresa import Empresa
from .usuario import Usuario


class Auditoria(CreatedModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="auditorias")
    usuario = models.ForeignKey(
        Usuario, on_delete=models.SET_NULL, related_name="auditorias", blank=True, null=True
    )
    entidade = models.CharField(max_length=60)
    entidade_id = models.UUIDField(blank=True, null=True)
    acao = models.CharField(max_length=20)
    dados_antes = models.JSONField(blank=True, null=True)
    dados_depois = models.JSONField(blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True)
    user_agent = models.CharField(max_length=255, blank=True)

    class Meta:
        db_table = "auditoria"
        verbose_name = "Auditoria"
        verbose_name_plural = "Auditorias"
        ordering = ["-criado_em"]

    def __str__(self) -> str:
        return f"{self.entidade} {self.acao}"
