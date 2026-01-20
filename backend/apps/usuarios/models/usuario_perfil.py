from django.db import models

from apps.core.models import UUIDModel


class UsuarioPerfil(UUIDModel):
    usuario = models.ForeignKey("usuarios.Usuario", on_delete=models.CASCADE)
    perfil = models.ForeignKey("usuarios.Perfil", on_delete=models.CASCADE)
    criado_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "usuarios_perfis"
        constraints = [
            models.UniqueConstraint(
                fields=["usuario", "perfil"],
                name="uq_usuario_perfil",
            )
        ]

    def __str__(self) -> str:
        return f"{self.usuario_id} - {self.perfil_id}"
