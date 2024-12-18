from django.urls import reverse
import pytest
from portfolio.base.models import Contato


@pytest.fixture
def resposta(client, db):
    resp = client.post(reverse('base:home'), data={'nome': Contato})
    return resp


@pytest.fixture
def resposta_dados_invalidos(client, db):
    resp = client.post(reverse('base:home'), data={'nome': Contato})
    return resp
