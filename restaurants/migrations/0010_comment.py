# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0009_auto_20151010_0030'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('content', models.CharField(max_length=200)),
                ('user', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('date_time', models.DateTimeField()),
                ('restaurant', models.ForeignKey(to='restaurants.Restaurant')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
