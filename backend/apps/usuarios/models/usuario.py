from django.db import models

from apps.core.models import UUIDModel


class Usuario(UUIDModel):
    empresa = models.ForeignKey("tenants.Empresa", on_delete=models.CASCADE)
    nome = models.CharField(max_length=180)
    email = models.EmailField(max_length=180)
    senha_hash = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    ultimo_login_em = models.DateTimeField(blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "usuarios"
        constraints = [
            models.UniqueConstraint(
                fields=["empresa", "email"],
                name="uq_usuario_empresa_email",
            )
        ]

    def __str__(self) -> str:
        return self.email
