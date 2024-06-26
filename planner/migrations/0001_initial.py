# Generated by Django 5.0.4 on 2024-04-30 03:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plantrip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('departure', models.CharField(max_length=20)),
                ('destination', models.CharField(max_length=255)),
                ('startdate', models.DateField()),
                ('enddate', models.DateField()),
                ('starttime', models.DateTimeField()),
                ('endtime', models.DateTimeField()),
                ('grouptrip', models.BooleanField(default=False)),
                ('solotrip', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Tourguide',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='images/default.jpg', null=True, upload_to='images/')),
            ],
        ),
    ]
