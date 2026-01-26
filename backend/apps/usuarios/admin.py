from django.contrib import admin

from .models import Perfil, Usuario, UsuarioPerfil


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id", "empresa", "nome", "email", "ativo", "criado_em")
    search_fields = ("nome", "email")
    list_filter = ("ativo", "empresa")
    ordering = ("-criado_em",)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ("id", "empresa", "nome", "descricao")
    search_fields = ("nome", "descricao")
    list_filter = ("empresa",)
    ordering = ("nome",)


@admin.register(UsuarioPerfil)
class UsuarioPerfilAdmin(admin.ModelAdmin):
    list_display = ("id", "usuario", "perfil", "criado_em")
    search_fields = ("usuario__email", "perfil__nome")
    list_filter = ("perfil__empresa",)
    ordering = ("-criado_em",)
