# coding:utf8
from django.conf.urls import patterns, url
from webLH import views

urlpatterns = patterns('',
                       url(r'^$', views.index, name='index'),
                       url(r'^login$', views.login, name='login'),
                       )
