# coding: utf-8

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from webLH.models import *


# Create your views here.


def index(request):
    more_than_five = date.today().year - int(settings.IS_OLD) > int(settings.SITE_SINCE)
    return render(request, 'index.html', {'page': 'inicio', 'more_than_five': more_than_five})


def login(request):
    mail = request.POST['mail']
    try:
        user = Usuario.objects.get(mail=mail)
    except (KeyError, Usuario.DoesNotExist):
        return HttpResponse(json.dumps({'msg': False}), content_type="application/json")
    else:
        result = user.isPassCorrect(request.POST['psw'])
        return HttpResponse(json.dumps({'msg': result}), content_type="application/json")