from rest_framework import serializers

from .models import Empresa, Usuario


class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = [
            "id",
            "razao_social",
            "nome_fantasia",
            "cnpj",
            "email",
            "telefone",
            "ativa",
            "criada_em",
            "atualizada_em",
        ]
        read_only_fields = ["id", "criada_em", "atualizada_em"]


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = [
            "id",
            "empresa",
            "nome",
            "email",
            "senha_hash",
            "ativo",
            "ultimo_login_em",
            "criado_em",
            "atualizado_em",
        ]
        read_only_fields = ["id", "criado_em", "atualizado_em"]
