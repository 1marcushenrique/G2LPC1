# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-20 23:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('votacao', '0003_candidato'),
    ]

    operations = [
        migrations.CreateModel(
            name='Token',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numero', models.CharField(max_length=10, verbose_name='Numero: ')),
            ],
        ),
    ]
