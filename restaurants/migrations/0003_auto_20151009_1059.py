# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_remove_food_restaurant'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='comment',
        ),
        migrations.AddField(
            model_name='food',
            name='restaurant',
            field=models.ForeignKey(default=1, to='restaurants.Restaurant'),
            preserve_default=False,
        ),
    ]
