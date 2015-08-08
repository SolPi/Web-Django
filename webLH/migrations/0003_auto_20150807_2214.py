# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webLH', '0002_auto_20150807_1807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
        ),
        migrations.CreateModel(
            name='InfoPermiso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permiso', models.IntegerField()),
                ('desc', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Permiso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permiso', models.IntegerField()),
                ('grupo', models.ForeignKey(blank=True, to='webLH.Grupo', null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.CharField(max_length=200)),
                ('psw', models.CharField(max_length=200)),
                ('state', models.IntegerField()),
                ('date_last_login', models.DateTimeField(verbose_name=b'date published')),
            ],
        ),
        migrations.RemoveField(
            model_name='permisos',
            name='user',
        ),
        migrations.RemoveField(
            model_name='user',
            name='grupo',
        ),
        migrations.AlterField(
            model_name='hermano',
            name='user',
            field=models.ForeignKey(to='webLH.Usuario'),
        ),
        migrations.DeleteModel(
            name='Grupos',
        ),
        migrations.DeleteModel(
            name='Permisos',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AddField(
            model_name='permiso',
            name='user',
            field=models.ForeignKey(blank=True, to='webLH.Usuario', null=True),
        ),
        migrations.AddField(
            model_name='grupo',
            name='user',
            field=models.ForeignKey(blank=True, to='webLH.Usuario', null=True),
        ),
    ]
