from django.contrib import admin
from django.urls import path


urlpatterns = [
    path('useradminpanel/', admin.site.urls),

]
