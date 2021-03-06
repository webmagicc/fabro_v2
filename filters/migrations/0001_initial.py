# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-26 07:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilterCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('published', models.BooleanField(default=True, help_text='Decides whether entity should be treated as active.', verbose_name='Published')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ordering')),
                ('name', models.CharField(default='', max_length=250, verbose_name='Name')),
                ('slug', models.CharField(blank=True, db_index=True, default='', max_length=250, verbose_name='Slug')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filtercategories', to='shop.Category', verbose_name='Category')),
            ],
            options={
                'verbose_name_plural': 'Filters Category',
                'verbose_name': 'Filter Category',
            },
        ),
        migrations.CreateModel(
            name='FilterSelect',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('published', models.BooleanField(default=True, help_text='Decides whether entity should be treated as active.', verbose_name='Published')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ordering')),
                ('name', models.CharField(default='', max_length=250, verbose_name='Name')),
                ('slug', models.CharField(blank=True, db_index=True, default='', max_length=250, verbose_name='Slug')),
                ('filter_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='filterselect', to='filters.FilterCategory', verbose_name='Filter Category')),
            ],
            options={
                'verbose_name_plural': 'Filters Select',
                'verbose_name': 'Filter Select',
            },
        ),
        migrations.CreateModel(
            name='ProductFilter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Modification date')),
                ('published', models.BooleanField(default=True, help_text='Decides whether entity should be treated as active.', verbose_name='Published')),
                ('ordering', models.IntegerField(blank=True, default=0, null=True, verbose_name='Ordering')),
                ('filter_category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filter_select_product', to='filters.FilterCategory', verbose_name='Filter Category')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='filterproducts', to='shop.Product', verbose_name='Product')),
                ('values', models.ManyToManyField(blank=True, related_name='filtervalues', to='filters.FilterSelect', verbose_name='Values')),
            ],
            options={
                'verbose_name_plural': 'Product Filters',
                'verbose_name': 'Product Filter',
            },
        ),
    ]
