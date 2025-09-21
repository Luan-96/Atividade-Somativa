from src import app, quotes

# Teste 1: Verifica se a página inicial está funcionando (Status Code)
def test_home_status_code():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

# Teste 2: Verifica o conteúdo HTML da página inicial
def test_home_content():
    client = app.test_client()
    response = client.get('/')
    response_text = response.data.decode('utf-8')
    assert "API de Citações" in response_text
    assert "Para obter uma citação aleatória" in response_text

# Teste 3: Verifica se a rota de citação retorna o status 200 (OK)
def test_quote_status_code():
    client = app.test_client()
    response = client.get('/quote')
    assert response.status_code == 200

# Teste 4: Verifica o tipo de conteúdo (Content-Type) da rota de citação
def test_quote_content_type():
    client = app.test_client()
    response = client.get('/quote')
    assert response.content_type == 'application/json'

# Teste 5: Verifica se a citação retornada é válida e pertence à lista original
def test_quote_is_valid():
    client = app.test_client()
    response = client.get('/quote')
    json_data = response.get_json()

    assert "citacao" in json_data
    assert isinstance(json_data["citacao"], str)
    assert json_data["citacao"] in quotes


# Teste 6: Verifica a estrutura do JSON retornado
def test_quote_json_structure():
    client = app.test_client()
    response = client.get('/quote')
    json_data = response.get_json()

    assert len(json_data.keys()) == 1
    assert "citacao" in json_data


# Teste 7: Garante que a codificação de caracteres é UTF-8
def test_character_encoding():
    client = app.test_client()
    response = client.get('/quote')
    # O charset faz parte do cabeçalho Content-Type
    assert 'utf-8' in response.charset.lower()

# Teste 8: Verifica o comportamento para uma rota inexistente (erro 404)
def test_404_not_found():
    client = app.test_client()
    response = client.get('/rota-que-nao-existe-de-verdade')
    assert response.status_code == 404