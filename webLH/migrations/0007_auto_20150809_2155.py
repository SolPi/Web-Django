# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webLH', '0006_auto_20150809_0912'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='date_alta',
            field=models.DateTimeField(null=True, verbose_name=b'date published', blank=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='date_last_login',
            field=models.DateTimeField(null=True, verbose_name=b'date published', blank=True),
        ),
    ]
