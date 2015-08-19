# coding:utf8
from django.conf.urls import patterns, url

from webLH import views


urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^login$', views.login, name='login'),
                       url(r'^resgistrar$', views.registrar, name='resgistrar'),
                       url(r'^(?P<question_id>\d+)/confirmar$', views.confirmar, name='confirmar'),
                       )
