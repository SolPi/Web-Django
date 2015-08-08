# coding:utf8
import json
from datetime import date

from django.db import models

from Utils.StringFn import *


# Create your models here.
class Usuario(models.Model):
    mail = models.CharField(max_length=200)
    psw = models.CharField(max_length=200, null=True, blank=True)
    state = models.IntegerField(default=0)
    date_last_login = models.DateTimeField('date published')

    def __str__(self):
        return self.mail.encode('utf-8')

    def save(self, *args, **kwargs):
        self.psw = cryptoSHA256(self.psw)
        super(Usuario, self).save(*args, **kwargs)

    def register(self):
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
        return self.permiso.permiso.encode('utf-8')
