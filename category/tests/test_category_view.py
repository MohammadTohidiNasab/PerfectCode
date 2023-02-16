def test_category_view(client):
    response = client.get(path = '/')
    assert response.status_code == 200


#account test
def test_account_login(client):
    response = client.get(path = '/account/login')
    assert response.status_code == 200


def test_account_register(client):
    response = client.get(path = '/account/otplogin')
    assert response.status_code == 200


def test_account_logout(client):
    response = client.get(path = '/account/logout')
    assert response.status_code == 302
