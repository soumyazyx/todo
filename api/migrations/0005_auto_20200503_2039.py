# Generated by Django 3.0.4 on 2020-05-03 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_task__list'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='_list',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='api.List'),
        ),
    ]
