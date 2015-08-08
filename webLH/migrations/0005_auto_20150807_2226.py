# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webLH', '0004_auto_20150807_2223'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infopermiso',
            name='permiso',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='permiso',
            name='permiso',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='state',
            field=models.IntegerField(default=0),
        ),
    ]
