# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_order_dostavka'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phon',
            field=models.CharField(verbose_name='Телефон', max_length=11, default=''),
        ),
        migrations.AlterField(
            model_name='order',
            name='dostavka',
            field=models.CharField(verbose_name='Способ доставки', max_length=250, default=''),
        ),
    ]
