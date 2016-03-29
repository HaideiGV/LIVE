# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('liveupdate', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('subject', models.CharField(max_length=10)),
                ('date', models.DateTimeField(default=datetime.datetime(2016, 3, 28, 16, 40, 43, 804830))),
                ('email', models.EmailField(max_length=254)),
                ('text', models.TextField(max_length=100)),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
        migrations.CreateModel(
            name='LinkRateEvent',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('is_like', models.BooleanField(default=False)),
                ('link', models.ForeignKey(to='liveupdate.Links')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-is_like'],
            },
        ),
        migrations.DeleteModel(
            name='ViewAllTypeFields',
        ),
    ]
