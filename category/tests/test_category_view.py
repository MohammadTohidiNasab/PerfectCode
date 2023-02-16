from django.test import Client, TestCase
import pytest
from account.models import User


def test_category_view(client):
    response = client.get(path = '/')
    assert response.status_code == 200


#account test
def test_account_login(client):
    response = client.get(path = '/account/login')
    assert response.status_code == 200


class TestPageLogin(TestCase):
   def setUp(self):
       self.client = Client()
   def test_login_page(self):
       response = self.client.get(path = '/account/login')
       self.assertEqual(response.status_code, 200)
       self.assertTemplateUsed(response, 'account/login.html')


def test_account_register(client):
    response = client.get(path = '/account/otplogin')
    assert response.status_code == 200


@pytest.mark.django_db
def test_account_signup(client):
    user = User.objects.create_user('username','password')
    client.login(fullname=user.fullname,password='password')
    response = client.get(path = '/account/otplogin',follow=True)
    assert response.status_code == 200


def test_account_logout(client):
    response = client.get(path = '/account/logout')
    assert response.status_code == 302
#finish account testing

