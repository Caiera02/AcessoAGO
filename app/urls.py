from django.contrib import admin
from django.urls import path
from login.views import  tela_login,lista_acessos,sorteador

urlpatterns = [
    path('admin/', admin.site.urls , name='admin'),
    # Rota para a tela de identificação (Nome e Matrícula)
    path('cadastro/', tela_login, name='tela_login'),
    path('sorteador', sorteador, name='sorteio'),
    
    # Rota para a página que será exibida após o acesso liberado
    # path('sucesso/', pagina_liberada, name='pagina_liberada'),
    
    # Rota para você visualizar a lista de todos que acessaram
    path('relatorio-acessos/', lista_acessos, name='lista_acessos'),
]
