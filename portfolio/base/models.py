from django.db import models

    
class Comentario(models.Model):
    nome = models.CharField(max_length=128)
    feita = models.BooleanField(default=False)

from django.db import models

class Produto(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name
