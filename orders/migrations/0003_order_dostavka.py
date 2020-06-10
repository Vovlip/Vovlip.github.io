# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200602_1145'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='dostavka',
            field=models.CharField(verbose_name='Способ доставки', max_length=250, default='SOME STRING'),
        ),
    ]
