from django.urls import path
from .views import lista_usuario,cria_usuario,altera_usuario,deleta_usuario

urlpatterns = [
    path('listar/', lista_usuario, name='lista_usuario'),
    path('novo', cria_usuario, name='cria_usuario'),
    path('alterar/<int:id>/', altera_usuario, name='altera_usuario'),
    path('apagar/<int:id>/', deleta_usuario, name='deleta_usuario'),

]