from django.contrib import admin

from .models import Empresa, Usuario


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("razao_social", "cnpj", "ativa", "criada_em")
    search_fields = ("razao_social", "nome_fantasia", "cnpj")
    list_filter = ("ativa",)


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("nome", "email", "empresa", "ativo", "criado_em")
    search_fields = ("nome", "email")
    list_filter = ("ativo", "empresa")
