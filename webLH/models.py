# coding:utf8
from Utils.StringFn import *
from datetime import date
from django.db import models
import json


# Create your models here.
class Usuario(models.Model):
    mail = models.CharField(max_length=200)
    psw = models.CharField(max_length=200, null=True, blank=True)
    state = models.IntegerField(default=0)
    date_last_login = models.DateTimeField('date published', null=True, blank=True)
    date_alta = models.DateTimeField('date published', null=True, blank=True)

    def __str__(self):
        return self.mail.encode('utf-8')

    def save(self, *args, **kwargs):
        self.psw = cryptoSHA256(self.psw)
        super(Usuario, self).save(*args, **kwargs)

    def register(self):
        self.date_alta = date.today()
        self.save()

    def login(self, psw=str()):
        if self.isPassCorrect(psw):
            self.date_last_login = date.today()
            self.save()
            return True
        else:
            return False

    def isPassCorrect(self, psw=str()):
        return self.psw == cryptoSHA256(psw)

    def toJSON(self):
        return json.dumps({
            'id': self.id.encode('utf-8'),
            'mail': self.mail.encode('utf-8'),
            'date_last_login': self.date_last_login.strftime("%Y-%m-%d %H:%M:%S"),
        })


class Hermano(models.Model):
    user = models.ForeignKey(Usuario)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    apellidos = models.CharField(max_length=200, null=True, blank=True)
    tlf = models.CharField(max_length=200, null=True, blank=True)
    tlf2 = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    address2 = models.CharField(max_length=200, null=True, blank=True)
    grado = models.CharField(max_length=200, null=True, blank=True)
    status = models.CharField(max_length=200, null=True, blank=True)
    des_corta = models.CharField(max_length=200, null=True, blank=True)
    des_larga = models.CharField(max_length=200, null=True, blank=True)
    msg_motivacion = models.CharField(max_length=200, null=True, blank=True)
    fecha_nac = models.DateTimeField('date published')
    fecha_alta = models.DateTimeField('date published')

    def __str__(self):
        return self.nombre.encode('utf-8') + " " + self.apellidos.encode('utf-8')


class Grupo(models.Model):
    user = models.ForeignKey(Usuario)
    grupo = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.grupo.encode('utf-8')


class Permiso(models.Model):
    user = models.ForeignKey(Usuario, null=True, blank=True)
    grupo = models.ForeignKey(Grupo, null=True, blank=True)
    permiso = models.IntegerField(default=0)

    def __str__(self):
        return self.permiso.encode('utf-8')


class InfoPermiso(models.Model):
    permiso = models.IntegerField(default=0)
    desc = models.CharField(max_length=2000)

    def __str__(self):
        return self.permiso.encode('utf-8')

class Actividade(models.Model):
    permiso = models.ForeignKey(Permiso, null=True, blank=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    desc = models.CharField(max_length=2000, null=True, blank=True)
    date = models.DateTimeField('date published', null=True, blank=True)
    priority = models.IntegerField(default=2)  # 1: PRIORITY_ACTIVITY_HIGHLIGHT, 2: PRIORITY_ACTIVITY_NORMAL, 3: PRIORITY_ACTIVITY_OLD
    urlInPage = models.CharField(max_length=300, null=True, blank=True)  # la url donde se vera en detalle?
    

    def __str__(self):
        return "-titulo actividad: " + self.title.encode('utf-8') + "-----fecha: " 

class Photo(models.Model):
    actividad = models.ForeignKey(Actividade, null=True, blank=True)
    user = models.ForeignKey(Hermano, null=True, blank=True)
    urlBigPhoto = models.CharField(max_length=300, null=True, blank=True)  # url foto peq
    urlSmallPhoto = models.CharField(max_length=300, null=True, blank=True)  # rul foto grande
    isPagPpal = models.IntegerField(default=0)  # 1: true 0: false
    isForActivity = models.IntegerField(default=0)
    isForHermano = models.IntegerField(default=0)
    isForTitle = models.IntegerField(default=0)
    isForDescription = models.IntegerField(default=0)
    isforColumn = models.IntegerField(default=0)
    priority = models.IntegerField(default=1)  # (Prioridad 1 max). Si coincide, la más reciente(por fecha)
    date = models.DateTimeField('date published', null=True, blank=True)

    def __str__(self):
        return " Pagina ppal:" + self.isPagPpal + " Pagina activity:" + self.isForActivity + " Es para Hermano:" + self.isForHermano + " URL photo :" + self.urlBigPhoto
