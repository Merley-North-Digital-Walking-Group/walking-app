# Generated by Django 3.2.12 on 2022-02-08 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0004_delete_group_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='group',
            name='group_photo',
        ),
    ]
