from django.urls import reverse
import pytest
from portfolio.base.models import Comentario


'''@pytest.fixture
def resposta(client, db):
    resp = client.post(reverse('base:home'), data={'nome': 'Comentario'})
    return resp

def test_comentario_existe_no_bd(resposta):
    assert Comentario.objects.exists()

def test_redirect_depois_do_comentario(resposta):
    assert resposta.status_code == 302

@pytest.fixture
def resposta_dados_invalidos(client, db):
    resp = client.post(reverse('base:home'), data={'nome': ''})
    return resp

def test_comentario_nao_existe_no_bd(resposta_dado_invalido):
    assert not resposta_dado_invalido.Comentario.objects.exists()

def test_com_dados_invalidos(resposta_dado_invalido):
    assert resposta_dado_invalido.status_code == 400'''