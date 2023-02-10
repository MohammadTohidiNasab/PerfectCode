from rest_framework import viewsets
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .serializers import OrderingSerializer
from .models import Ordering
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

