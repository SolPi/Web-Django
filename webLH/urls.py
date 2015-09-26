# coding:utf8
from django.conf.urls import patterns, url

from webLH import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^login$', views.login, name='login'),
                       url(r'^inicio$', views.inicio, name='inicio'),
                       url(r'^actividades$', views.actividades, name='actividades'),
                       url(r'^socios$', views.socios, name='socios'),
                       url(r'^contacto$', views.contacto, name='contacto'),
                       url(r'^nuevo_socio$', views.nuevo_socio, name='nuevo_socio'),
                       url(r'^resgistrar$', views.registrar, name='resgistrar'),
                       url(r'^(?P<question_id>\d+)/confirmar$', views.confirmar, name='confirmar'),
                       )
