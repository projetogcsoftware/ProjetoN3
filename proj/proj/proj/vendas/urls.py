from django.urls import path
from .views import lista_venda,cria_venda,altera_venda,deleta_venda,lista_mesa,cria_mesa

urlpatterns = [
    path('listar/', lista_venda, name='lista_venda'),
    path('novo/<int:mesa>/', cria_venda, name='cria_venda'),
    path('alterar/<int:id>/', altera_venda, name='altera_venda'),
    path('apagar/<int:id>/', deleta_venda, name='deleta_venda'),

    path('listar_mesa/', lista_mesa, name='lista_mesa'),
    path('novo_mesa', cria_mesa, name='cria_mesa'),
]