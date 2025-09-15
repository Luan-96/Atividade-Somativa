# test_app.py

from app import app

def test_home():
    """ Teste para a rota principal (home). """
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert b"API de Citações" in response.data

def test_quote():
    """ Teste para a rota de citações. """
    client = app.test_client()
    response = client.get('/quote')
    assert response.status_code == 200
    # Verifica se a resposta é um JSON válido
    assert response.is_json
    json_data = response.get_json()
    # Verifica se a chave 'citacao' existe no JSON
    assert "citacao" in json_data