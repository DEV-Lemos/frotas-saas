from django.db import models

from .base import CreatedModel
from .perfil import Perfil
from .usuario import Usuario


class UsuarioPerfil(CreatedModel):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="perfis")
    perfil = models.ForeignKey(Perfil, on_delete=models.CASCADE, related_name="usuarios")

    class Meta:
        db_table = "usuarios_perfis"
        verbose_name = "Usuário Perfil"
        verbose_name_plural = "Usuários Perfis"
        constraints = [
            models.UniqueConstraint(
                fields=["usuario", "perfil"], name="uq_usuario_perfil"
            )
        ]

    def __str__(self) -> str:
        return f"{self.usuario} - {self.perfil}"
