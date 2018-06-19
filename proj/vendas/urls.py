from django.urls import path
from .views import lista_venda,cria_venda,altera_venda,deleta_venda,lista_venda_pedido

urlpatterns = [
    path('listar/', lista_venda, name='lista_venda'),
    #path('listarr/', lista_venda_pedido, name='lista_venda_pedido'),
    path('novo/', cria_venda, name='cria_venda'),
    path('alterar/<int:id>/', altera_venda, name='altera_venda'),
    path('apagar/<int:id>/', deleta_venda, name='deleta_venda'),

]