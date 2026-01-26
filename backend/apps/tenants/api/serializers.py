import re

from rest_framework import serializers

from apps.tenants.models import Empresa


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

    def validate_cnpj(self, value):
        if not value:
            return value

        digits = re.sub(r"\D", "", value)
        if len(digits) != 14:
            raise serializers.ValidationError("CNPJ deve ter 14 digitos.")

        return digits

    def validate_email(self, value):
        if not value:
            return value
        return value.strip().lower()
