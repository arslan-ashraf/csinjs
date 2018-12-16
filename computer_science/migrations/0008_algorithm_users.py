# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-12-16 01:17
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('computer_science', '0007_algorithm_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='algorithm',
            name='users',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]