# Generated by Django 3.2 on 2021-04-21 07:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('movies', '0001_initial'),
        ('books', '0001_initial'),
        ('favs', '0002_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fav',
            new_name='Favs',
        ),
    ]
