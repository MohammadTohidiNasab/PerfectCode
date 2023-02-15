def test_category_view(client):
    response = client.get(path = '/')
    assert response.status_code == 200


