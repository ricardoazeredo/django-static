from django.contrib import admin
from .models import Funcionarios

@admin.register(Funcionarios)
class FuncionariosAdmin(admin.ModelAdmin):
    # Quais colunas mostrar na lista de produtos
    list_display = ('nome', 'cargo', 'departamento', 'data_contratacao','status')
    # Por quais campos podemos buscar
    search_fields = ("nome",)
    # Quais campos podemos filtrar
    list_filter = ('status', 'data_contratacao')
    
# admin.site.register(Funcionarios)


    