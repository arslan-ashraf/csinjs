# Generated by Django 2.1.1 on 2018-09-14 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computer_science', '0005_auto_20180913_1812'),
    ]

    operations = [
        migrations.AlterField(
            model_name='algorithm',
            name='friendly_title',
            field=models.SlugField(default=None),
        ),
    ]