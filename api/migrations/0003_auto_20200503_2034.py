# Generated by Django 3.0.4 on 2020-05-03 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_list'),
    ]

    operations = [
        migrations.RenameField(
            model_name='list',
            old_name='list_title',
            new_name='title',
        ),
    ]