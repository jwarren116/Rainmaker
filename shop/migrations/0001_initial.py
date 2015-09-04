# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=63)),
                ('description', models.CharField(max_length=255, blank=True)),
                ('photo', models.ImageField(upload_to=b'products')),
                ('price', models.DecimalField(max_digits=9, decimal_places=2)),
                ('item_number', models.IntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
