# Generated by Django 3.1 on 2020-08-09 18:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Container',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=11)),
                ('carrier', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=200)),
                ('date', models.DateTimeField()),
                ('location', models.CharField(max_length=300)),
                ('last_import', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
    ]
