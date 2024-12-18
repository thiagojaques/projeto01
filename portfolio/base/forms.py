from django.forms import ModelForm
from portfolio.base.models import Contato


class Contato(ModelForm):
    class Meta:
        model = Contato
        fields = ['nome', 'email', 'mensagem']