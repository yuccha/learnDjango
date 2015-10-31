# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0008_auto_20151010_0029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='food',
            options={'ordering': ['price']},
        ),
    ]
