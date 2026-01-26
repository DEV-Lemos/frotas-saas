from django.contrib.auth.hashers import make_password
from rest_framework import serializers

from apps.usuarios.models import Perfil, Usuario, UsuarioPerfil


class UsuarioSerializer(serializers.ModelSerializer):
    senha = serializers.CharField(write_only=True, required=False, min_length=6)

    class Meta:
        model = Usuario
        fields = [
            "id",
            "empresa",
            "nome",
            "email",
            "senha",
            "ativo",
            "ultimo_login_em",
            "criado_em",
            "atualizado_em",
        ]
        read_only_fields = ["id", "empresa", "ultimo_login_em", "criado_em", "atualizado_em"]

    def validate_email(self, value):
        if not value:
            return value
        return value.strip().lower()

    def validate(self, attrs):
        request = self.context.get("request")
        empresa = getattr(request, "empresa", None)
        email = attrs.get("email") or getattr(self.instance, "email", None)

        if empresa and email:
            qs = Usuario.objects.filter(empresa=empresa, email=email)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError({"email": "Email ja existe para esta empresa."})

        return attrs

    def create(self, validated_data):
        senha = validated_data.pop("senha", None)
        if not senha:
            raise serializers.ValidationError({"senha": "Senha e obrigatoria."})
        validated_data["senha_hash"] = make_password(senha)
        return super().create(validated_data)

    def update(self, instance, validated_data):
        senha = validated_data.pop("senha", None)
        if senha:
            instance.senha_hash = make_password(senha)
        return super().update(instance, validated_data)


class PerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Perfil
        fields = ["id", "empresa", "nome", "descricao"]
        read_only_fields = ["id", "empresa"]

    def validate_nome(self, value):
        value = value.strip()
        if not value:
            raise serializers.ValidationError("Nome do perfil e obrigatorio.")
        return value

    def validate(self, attrs):
        request = self.context.get("request")
        empresa = getattr(request, "empresa", None)
        nome = attrs.get("nome") or getattr(self.instance, "nome", None)

        if empresa and nome:
            qs = Perfil.objects.filter(empresa=empresa, nome__iexact=nome)
            if self.instance:
                qs = qs.exclude(pk=self.instance.pk)
            if qs.exists():
                raise serializers.ValidationError({"nome": "Perfil ja existe para esta empresa."})

        return attrs


class UsuarioPerfilSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPerfil
        fields = ["id", "usuario", "perfil", "criado_em"]
        read_only_fields = ["id", "criado_em"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        request = self.context.get("request")
        empresa = getattr(request, "empresa", None)
        if empresa:
            self.fields["usuario"].queryset = Usuario.objects.filter(empresa=empresa)
            self.fields["perfil"].queryset = Perfil.objects.filter(empresa=empresa)

    def validate(self, attrs):
        usuario = attrs.get("usuario") or getattr(self.instance, "usuario", None)
        perfil = attrs.get("perfil") or getattr(self.instance, "perfil", None)

        if usuario and perfil and usuario.empresa_id != perfil.empresa_id:
            raise serializers.ValidationError("Usuario e perfil devem pertencer a mesma empresa.")

        request = self.context.get("request")
        empresa = getattr(request, "empresa", None)
        if empresa:
            if usuario and usuario.empresa_id != empresa.id:
                raise serializers.ValidationError({"usuario": "Usuario fora da empresa informada."})
            if perfil and perfil.empresa_id != empresa.id:
                raise serializers.ValidationError({"perfil": "Perfil fora da empresa informada."})

        return attrs
