# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('liveupdate', '0003_auto_20160328_1643'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=200, unique=True, default='Unknown'),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2017, 11, 27, 23, 40, 7, 826514)),
        ),
    ]
