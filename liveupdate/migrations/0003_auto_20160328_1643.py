# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('liveupdate', '0002_auto_20160328_1640'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2016, 3, 28, 16, 43, 29, 704114)),
        ),
    ]
