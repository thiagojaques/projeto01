from django.db import models

    
class Contato(models.Model):
    nome = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    mensagem = models.CharField(max_length=128)