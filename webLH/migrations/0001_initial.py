# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hermano',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.CharField(max_length=200)),
                ('psw', models.CharField(max_length=200)),
                ('nombre', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('tlf', models.CharField(max_length=200)),
                ('tlf2', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('address2', models.CharField(max_length=200)),
                ('grado', models.CharField(max_length=200)),
                ('fecha_nac', models.DateTimeField(verbose_name=b'date published')),
                ('fecha_alta', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
    ]
