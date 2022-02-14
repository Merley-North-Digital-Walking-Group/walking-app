# Generated by Django 3.2.11 on 2022-02-14 18:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0005_remove_group_group_photo'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0002_user_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='App_User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DOB', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=100)),
                ('group', models.ManyToManyField(to='groups.Group')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]
