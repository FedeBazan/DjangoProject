from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def bienvenido(request):
    return HttpResponse('<h1>Hola Mundo</h1>')

def despedirse(request):
    return HttpResponse('<h1>Despedida desde Django</h1>')

def contacto(request):
    return HttpResponse('''<h2>Contacto</h2>
    <ul>
        <li>Name: julio Pablo Federico</li>
        <li>Surname: Bazan</li>
        <li>Cell-Phone: 123123123</li>
    </ul>''')