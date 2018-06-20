from django.db import models

# Create your models here.

class Venda(models.Model):
    item = models.IntegerField();
    mesa = models.IntegerField();
    descricao = models.CharField(max_length=40);
    qtd = models.IntegerField();
    valor_unit = models.DecimalField(max_digits=7, decimal_places=2);
    situ = models.IntegerField();

class Mesa(models.Model):
    numero = models.IntegerField();
    situ = models.IntegerField();
