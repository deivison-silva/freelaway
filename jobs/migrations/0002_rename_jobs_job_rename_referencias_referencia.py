# Generated by Django 4.0.3 on 2022-04-06 14:04

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('jobs', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Jobs',
            new_name='Job',
        ),
        migrations.RenameModel(
            old_name='Referencias',
            new_name='Referencia',
        ),
    ]