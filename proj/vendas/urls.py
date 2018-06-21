from django.urls import path
from .views import lista_venda,cria_venda,altera_venda,deleta_venda,lista_mesa,cria_mesa,fecha_venda,libera_produto
from .rel_vendas import some_view
urlpatterns = [
    path('listar/', lista_venda, name='lista_venda'),
    path('novo/<int:mesa>/', cria_venda, name='cria_venda'),
    path('fecha/<int:mesa>/', fecha_venda, name='fecha_venda'),
    path('libera/<int:mesa>/', libera_produto, name='libera_produto'),
    path('alterar/<int:id>/', altera_venda, name='altera_venda'),
    path('apagar/<int:id>/', deleta_venda, name='deleta_venda'),
    path('listar_mesa/', lista_mesa, name='lista_mesa'),
    path('novo_mesa', cria_mesa, name='cria_mesa'),
    path('pdf/',some_view,name='some_view'),

]