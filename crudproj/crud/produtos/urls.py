from django.urls import path
from .views import home,cria_produto,altera_produto,deleta_produto
urlpatterns = [
    path('',home, name='lista_produto'),
    path('novo',cria_produto, name='cria_produto'),
    path('alterar/<int:id>/',altera_produto, name='altera_produto'),
    path('apagar/<int:id>/',deleta_produto, name='deleta_produto'),
]

