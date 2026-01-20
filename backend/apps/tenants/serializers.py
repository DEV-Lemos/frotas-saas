from rest_framework import serializers

from .models import Empresa


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
