# Register your models here.
from django.contrib import admin

from .models import Empresa


@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    list_display = ("id", "razao_social", "nome_fantasia", "cnpj", "ativa", "criada_em")
    search_fields = ("razao_social", "nome_fantasia", "cnpj")
    list_filter = ("ativa",)
    ordering = ("-criada_em",)
