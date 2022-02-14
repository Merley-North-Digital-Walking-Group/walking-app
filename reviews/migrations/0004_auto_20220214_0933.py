# Generated by Django 3.2.11 on 2022-02-14 09:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('walks', '0007_auto_20220211_1515'),
        ('reviews', '0003_auto_20220208_1548'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='content',
            new_name='body',
        ),
        migrations.AddField(
            model_name='review',
            name='author',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='review',
            name='walk_ID',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='walks.walk'),
        ),
        migrations.AlterField(
            model_name='review',
            name='walk_rating',
            field=models.IntegerField(blank=True, choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
    ]
