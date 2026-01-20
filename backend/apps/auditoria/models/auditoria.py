from django.db import models

from apps.core.models import UUIDModel


class Auditoria(UUIDModel):
    ACAO_CHOICES = [
        ("CRIAR", "CRIAR"),
        ("ATUALIZAR", "ATUALIZAR"),
        ("EXCLUIR", "EXCLUIR"),
        ("LOGIN", "LOGIN"),
        ("LOGOUT", "LOGOUT"),
    ]

    empresa = models.ForeignKey("tenants.Empresa", on_delete=models.CASCADE)
    usuario = models.ForeignKey(
        "usuarios.Usuario",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    entidade = models.CharField(max_length=60)
    entidade_id = models.UUIDField(blank=True, null=True)
    acao = models.CharField(max_length=20, choices=ACAO_CHOICES)
    dados_antes = models.JSONField(blank=True, null=True)
    dados_depois = models.JSONField(blank=True, null=True)
    ip = models.CharField(max_length=45, blank=True, null=True)
    user_agent = models.CharField(max_length=255, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "auditoria"

    def __str__(self) -> str:
        return f"{self.entidade} - {self.acao}"
