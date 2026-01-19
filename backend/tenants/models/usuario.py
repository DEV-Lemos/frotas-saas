from django.db import models

from .base import TimestampedModel
from .empresa import Empresa


class Usuario(TimestampedModel):
    empresa = models.ForeignKey(Empresa, on_delete=models.CASCADE, related_name="usuarios")

    nome = models.CharField(max_length=180)
    email = models.EmailField(max_length=180)
    senha_hash = models.CharField(max_length=255)

    ativo = models.BooleanField(default=True)
    ultimo_login_em = models.DateTimeField(blank=True, null=True)

    class Meta:
        db_table = "usuarios"
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"
        ordering = ["nome"]
        constraints = [
            models.UniqueConstraint(
                fields=["empresa", "email"], name="uq_usuario_empresa_email"
            )
        ]

    def __str__(self) -> str:
        return self.nome
