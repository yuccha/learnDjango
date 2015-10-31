# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0003_auto_20151009_1059'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='comment',
            field=models.CharField(max_length=50, blank=True),
            preserve_default=True,
        ),
    ]
