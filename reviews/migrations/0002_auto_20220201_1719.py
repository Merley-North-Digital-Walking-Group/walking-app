# Generated by Django 3.2.11 on 2022-02-01 17:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approve_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='disapprove_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='comment',
            name='photo',
            field=models.ImageField(default=None, height_field=768, upload_to='', width_field=1024),
        ),
        migrations.AddField(
            model_name='review',
            name='approve_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='disapprove_count',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='review',
            name='photo',
            field=models.ImageField(default=None, height_field=768, upload_to='', width_field=1024),
        ),
        migrations.AddField(
            model_name='review',
            name='walk_rating',
            field=models.IntegerField(default=1, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
