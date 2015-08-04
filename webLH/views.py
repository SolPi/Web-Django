# coding:utf8

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from datetime import date
from django.conf import settings


# Create your views here.


def index(request):
	more_than_five = date.today().year - int(settings.IS_OLD) > int(settings.SITE_SINCE)
	return render(request, 'index.html', {'page':'init','more_than_five':more_than_five})

