# Generated by Django 3.2.11 on 2022-02-15 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('walks', '0007_auto_20220211_1515'),
        ('reviews', '0004_auto_20220214_0933'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='walk_ID',
        ),
        migrations.AddField(
            model_name='review',
            name='walk',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='walks.walk'),
        ),
    ]