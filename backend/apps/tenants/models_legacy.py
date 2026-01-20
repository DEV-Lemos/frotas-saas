import uuid

from django.core.validators import RegexValidator
from django.db import models


class Empresa(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    razao_social = models.CharField(max_length=180)
    nome_fantasia = models.CharField(max_length=180, blank=True)

    cnpj = models.CharField(
        max_length=14,
        blank=True,
        null=True,
        unique=True,
        validators=[
            RegexValidator(
                regex=r"^\d{14}$",
                message="CNPJ deve conter exatamente 14 dígitos (somente números).",
            )
        ],
        help_text="Somente números (14 dígitos).",
    )

    email = models.EmailField(max_length=180, blank=True)
    telefone = models.CharField(max_length=20, blank=True)

    ativa = models.BooleanField(default=True)

    criada_em = models.DateTimeField(auto_now_add=True)
    atualizada_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "empresas"
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"
        ordering = ["razao_social"]

    def __str__(self) -> str:
        return self.nome_fantasia or self.razao_social


class Usuarios(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_empresa = models.ForeignKey(
        Empresa,
        on_delete=models.CASCADE,
        verbose_name="Empresa",
    )
    nome = models.CharField(max_length=180, null=False, blank=False)
    email = models.EmailField(max_length=180, unique=True, null=False, blank=False)

    senha_hash = models.CharField(max_length=256, null=False, blank=False)
    ativo = models.BooleanField(default=True)
    ultimo_login_em = models.DateTimeField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "usuarios"
        constraints = [
            models.UniqueConstraint(fields=["empresa", "email"], name="uq_usuario_empresa_email")
        ]
        verbose_name = "Usuário"
        verbose_name_plural = "Usuários"

    def __str__(self) -> str:
        return self.email


class Perfis(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=100, unique=True, null=False, blank=False)
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    atualizado_em = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "perfis"
        verbose_name = "Perfil"
        verbose_name_plural = "Perfis"

    def __str__(self) -> str:
        return self.nome


class UsuarioPerfis(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    id_usuario = models.ForeignKey(
        Usuarios,
        on_delete=models.CASCADE,
        verbose_name="Usuário",
    )
    id_perfil = models.ForeignKey(
        Perfis,
        on_delete=models.CASCADE,
        verbose_name="Perfil",
    )
    atribuido_em = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "usuario_perfis"
        constraints = [
            models.UniqueConstraint(fields=["id_usuario", "id_perfil"], name="uq_usuario_perfil")
        ]
        verbose_name = "Usuário Perfil"
        verbose_name_plural = "Usuários Perfis"

    def __str__(self) -> str:
        return f"{self.id_usuario.email} - {self.id_perfil.nome}"
