# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webLH', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Grupos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permiso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Permisos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('permiso', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mail', models.CharField(max_length=200)),
                ('psw', models.CharField(max_length=200)),
                ('date_last_login', models.DateTimeField(verbose_name=b'date published')),
                ('grupo', models.ForeignKey(to='webLH.Grupos')),
            ],
        ),
        migrations.RemoveField(
            model_name='hermano',
            name='mail',
        ),
        migrations.RemoveField(
            model_name='hermano',
            name='psw',
        ),
        migrations.AlterField(
            model_name='hermano',
            name='address2',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='hermano',
            name='tlf2',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='permisos',
            name='user',
            field=models.ForeignKey(to='webLH.User'),
        ),
        migrations.AddField(
            model_name='hermano',
            name='user',
            field=models.ForeignKey(default=1, to='webLH.User'),
            preserve_default=False,
        ),
    ]
