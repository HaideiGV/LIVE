# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('liveupdate', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='links',
            name='linkUrl',
            field=models.URLField(unique=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='links',
            name='rating',
            field=models.IntegerField(default=0),
        ),
    ]
