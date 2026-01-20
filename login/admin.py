from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from login.models import Acesso, MatriculaAutorizada

@admin.register(MatriculaAutorizada)
class MatriculaAutorizadaAdmin(ImportExportModelAdmin):
    list_display = ('numero', 'nome_aluno')
    search_fields = ('numero', 'nome_aluno')
    # Isso permite que você importe uma planilha com a lista de quem pode acessar

@admin.register(Acesso)
class AcessoAdmin(ImportExportModelAdmin):
    list_display = ('nome', 'matricula', 'data_acesso')
    list_filter = ('data_acesso',)
    # Isso permite que você exporte todos os logs de acesso para Excel/CSV