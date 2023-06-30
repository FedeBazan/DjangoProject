from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.template import Template,context

# Create your views here.


def saludar(request):
    doc_externo=open('C:/Users/Canavire/pythonCourse/DjangoProject/DjangoProject/Proyecto1/HTML/miplantilla.html')
    plt=Template(doc_externo.read())
    doc_externo.close()
    conntexto=context()
    documento=plt.render(conntexto)
    return HttpResponse(documento)

def despedida(request):
    return HttpResponse('Adios')

def fechahora(request):
    fecha_actual=datetime.datetime.now()
    document= f'''Hora y decha actual={fecha_actual}
    '''
    return HttpResponse(document)

def calcula_edad(request,anio):
    edad_actual=18
    periodo=anio-2023
    edadfutura=edad_actual+periodo
    documento=f'''<html><body> en el año {anio} tendras {edadfutura} '''
    return HttpResponse(documento)

