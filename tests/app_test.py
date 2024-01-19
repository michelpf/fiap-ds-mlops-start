import src.app as app

def test_api_return():
    results = app.get_product(1)
    data = results.json()
    assert results.status_code == 200
    assert 'id' in data
    assert data['id'] == 1
