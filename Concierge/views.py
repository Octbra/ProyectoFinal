from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def inicio(request):
    return HttpResponse('<h1>Inicio</h1>')