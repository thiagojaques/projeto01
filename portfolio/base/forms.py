from django.forms import ModelForm
from portfolio.base.models import Comentario
from rest_framework import serializers
from .models import Produto


class Comentario(ModelForm):
    class Meta:
        model = Comentario
        fields = ['nome']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'