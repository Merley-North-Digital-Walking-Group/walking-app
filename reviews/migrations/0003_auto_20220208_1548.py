# Generated by Django 3.2.12 on 2022-02-08 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20220201_1719'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='review',
            name='photo',
        ),
    ]
