# Generated by Django 5.0.4 on 2024-05-01 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planner', '0002_alter_plantrip_starttime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='plantrip',
            name='endtime',
            field=models.TimeField(),
        ),
        migrations.AlterField(
            model_name='plantrip',
            name='starttime',
            field=models.TimeField(),
        ),
    ]
