from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=40)
    cargo = models.IntegerField()
    senha = models.CharField(max_length=5)
    cpf = models.CharField(max_length=12)
    endereco = models.TextField(max_length=70)
    telefone = models.CharField(max_length=12)