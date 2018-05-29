from django.urls import path
from .views import home,lista_produto_nome,cria_produto,altera_produto,deleta_produto

urlpatterns = [
    path('', home, name='lista_produto'),
    path('buscar', lista_produto_nome, name='lista_produto_nome'),
    path('novo', cria_produto, name='cria_produto'),
    path('alterar/<int:id>/', altera_produto, name='altera_produto'),
    path('apagar/<int:id>/', deleta_produto, name='deleta_produto'),

]