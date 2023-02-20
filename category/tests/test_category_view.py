from django.test import Client, TestCase
import pytest
from account.models import User
from category.models import Category
from.factory import UserFactory


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
    user = UserFactory()
    client.login(fullname=user.fullname,password='password')
    response = client.get(path = '/account/otplogin',follow=True)
    assert response.status_code == 200


def test_account_logout(client):
    response = client.get(path = '/account/logout')
    assert response.status_code == 302
#finish account testing


#start category test

def test_category_view(client):
    response = client.get(path = '/')
    assert response.status_code == 200


@pytest.mark.django_db
def test_add_category(client):
    newcategory = Category.objects.create(name='new category',description='its just test',slug='category')
    response = client.get(path='/category/api/')
    assert 200 == response.status_code
    assert 'new category' in str(response.content)
