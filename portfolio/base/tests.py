from django.urls import reverse
from pytest_django.asserts import assertContains
import pytest

@pytest.fixture
def resposta(client):
    resp = client.get(reverse('base:home'))
    return resp

def test_status_code(resposta):
    assert resposta.status_code == 200

def test_formulario_presente(resposta):
    assertContains(resposta, '<form')

def test_do_botao_salvar_presente(resposta):
    assertContains(resposta, '<button type="submit"')