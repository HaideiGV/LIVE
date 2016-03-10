# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Links',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('linkUrl', models.URLField(max_length=500)),
                ('rating', models.IntegerField()),
                ('description', models.CharField(max_length=500)),
                ('category', models.ForeignKey(related_name='+', to='liveupdate.Category')),
            ],
            options={
                'ordering': ['category'],
            },
        ),
        migrations.CreateModel(
            name='Update',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('text', models.CharField(max_length=200)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='ViewAllTypeFields',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bigint_field', models.BigIntegerField()),
                ('binary_field', models.BinaryField()),
                ('boolean_field', models.BooleanField()),
                ('char_field', models.CharField(max_length=10)),
                ('comma_separ_field', models.CommaSeparatedIntegerField(max_length=500)),
                ('date_field', models.DateField(auto_now_add=True)),
                ('datetime_field', models.DateTimeField()),
                ('decimal_field', models.DecimalField(max_digits=20, decimal_places=5)),
                ('email_field', models.EmailField(max_length=254)),
                ('float_field', models.FloatField()),
                ('integer_field', models.IntegerField()),
                ('ip_field', models.GenericIPAddressField(null=True)),
                ('null_bool_field', models.NullBooleanField()),
                ('positive_integer_field', models.PositiveIntegerField()),
                ('slug', models.SlugField()),
                ('text', models.TextField(max_length=100)),
                ('time', models.TimeField(auto_now=True)),
                ('url_field', models.URLField()),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]
