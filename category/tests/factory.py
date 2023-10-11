import factory
from account.models import User
from django.contrib.auth.hashers import make_password
from category.models import Category
from factory import fuzzy


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    User.fullname = factory.Sequence(lambda n: f"user_{n:04}")
    email = factory.LazyAttribute(lambda user: f"{User.fullname}@gmail.com")
    password = factory.LazyFunction(lambda: make_password("password"))


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = fuzzy.FuzzyText(length=20)
    description = fuzzy.FuzzyText(length=200)
    slug = fuzzy.FuzzyText(length=20)
