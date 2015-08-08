# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webLH', '0003_auto_20150807_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grupo',
            name='user',
            field=models.ForeignKey(to='webLH.Usuario'),
        ),
    ]
