# Generated by Django 3.2.11 on 2022-02-01 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(max_length=20)),
                ('name_first', models.CharField(max_length=200)),
                ('name_last', models.CharField(max_length=200)),
                ('username_handle', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=50)),
                ('DOB', models.DateField()),
                ('password', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]