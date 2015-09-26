# coding: utf-8

from django.http import HttpResponse
from django.shortcuts import render

from webLH.Utils.MailFn import *
from webLH.context_var import * 
from webLH.models import *


# Create your views here.
def index(request):
    return buildPage(request, {'page': 'inicio'})
def _index(request):
    return {}

def inicio(request):
    return buildPage(request, {'page': 'inicio'})
def _inicio(request):
    return {}

def actividades(request):
    return buildPage(request, {'page': 'actividades'})
def _actividades(request):
    activity_list = Actividade.objects.order_by('-date')[:]
    context = {'activity_list':activity_list}
    return context

def socios(request):
    return buildPage(request, {'page': 'socios'})
def _socios(request):
    return {}

def contacto(request):
    return buildPage(request, {'page': 'contacto'})
def _contacto(request):
    return {}

def nuevo_socio(request):
    return buildPage(request, {'page': 'nuevo_socio'})
def _nuevo_socio(request):
    return {}

def login(request):
    mail = request.POST['mail']
    try:
        user = Usuario.objects.get(mail=mail)
    except (KeyError, Usuario.DoesNotExist):
        return HttpResponse(json.dumps({'msg': False}), content_type="application/json")
    else:
        result = user.isPassCorrect(request.POST['pass'])
        return HttpResponse(json.dumps({'msg': result}), content_type="application/json")

def registrar(request):
    mail = request.POST['mail']
    try:
        user = Usuario.objects.get(mail=mail)
    except (KeyError, Usuario.DoesNotExist):
        psw = request.POST['pass']
        user = Usuario()
        user.mail = mail
        user.psw = psw
        
        user.state = STATE_REGISTER
        user.register()

        mail = Mail()
        mail.sendMesagge("garoz.daniel@gmail.com", "confirma tu cuenta", "<a href='http://localhost:8000/lh/confirmar?userId=" + user.id + "'>Pulsa para confirmar</a>")

        return HttpResponse(json.dumps({'msg': 'Usuario registrado'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'msg': 'Ese email ya existe, cuantas veces te vas a registrar?'}), content_type="application/json")

def confirmar(request, userId):
    user = Usuario.objects.get(id=userId)
    user.state = STATE_REGISTER_CONFIRM
    return render(request, 'index.html', {'page': 'new_socio'})

def buildPage(request, context):
    context.append(_index).append(_inicio).append(_actividades).append(_socios).append(_contacto).append(_nuevo_socio)
    return render(request, 'index.html', context)
