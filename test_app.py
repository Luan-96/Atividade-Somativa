from app import app


def test_home():
    client = app.test_client()
    response = client.get('/')

    response_text = response.data.decode('utf-8')

    assert response.status_code == 200
    assert "API de Citações" in response_text


def test_quote():
    client = app.test_client()
    response = client.get('/quote')
    assert response.status_code == 200
    assert response.is_json
    json_data = response.get_json()
    assert "citacao" in json_data