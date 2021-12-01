from django import urls
from django.urls.conf import path
from .views import inicio


urlspatterns = [
    path('', inicio, name='inicio')
]