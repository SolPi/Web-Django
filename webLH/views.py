# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse

from webLH.models import *
from webLH.Utils.MailFn import *
from webLH.context_var import *


# Create your views here.


def index(request):
    return render(request, 'index.html', {'page': 'new_socio'})


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
        mail.sendMesagge("garoz.daniel@gmail.com", "confirma tu cuenta", "<a href='http://localhost:8000/lh/confirmar?userId="+user.id+"'>Pulsa para confirmar</a>")

        return HttpResponse(json.dumps({'msg': 'Usuario registrado'}), content_type="application/json")
    else:
        return HttpResponse(json.dumps({'msg': 'Ese email ya existe, cuantas veces te vas a registrar?'}), content_type="application/json")

def confirmar(request, userId):
    user = Usuario.objects.get(id=userId)
    user.state = STATE_REGISTER_CONFIRM
    return render(request, 'index.html', {'page': 'new_socio'})
