# base/models.py
from django.db import models


class Contato(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField()
    mensagem = models.CharField(max_length=228)

    class Meta:
        db_table = 'base_contato'  # Nome da tabela
