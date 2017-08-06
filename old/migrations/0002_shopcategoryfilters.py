# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-29 11:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('old', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ShopCategoryfilters',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_id', models.IntegerField()),
                ('filter_id', models.IntegerField()),
                ('ordering', models.IntegerField()),
            ],
            options={
                'managed': False,
                'db_table': 'shop_categoryfilters',
            },
        ),
    ]