from django.db import models

from .base import CreatedModel
from .empresa import Empresa


class Anexo(CreatedModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="anexos")
    entidade = models.CharField(max_length=40)
    entidade_id = models.UUIDField()
    nome_arquivo = models.CharField(max_length=255)
    mime_type = models.CharField(max_length=100, blank=True)
    url_armazenamento = models.TextField()

    class Meta:
        db_table = "anexos"
        verbose_name = "Anexo"
        verbose_name_plural = "Anexos"
        ordering = ["-criado_em"]

    def __str__(self) -> str:
        return self.nome_arquivo
