# Generated by Django 2.2.5 on 2019-09-25 19:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190925_2129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutorial',
            name='tutorial_published',
            field=models.DateTimeField(default=datetime.datetime(2019, 9, 25, 21, 29, 30, 460790), verbose_name='date published'),
        ),
    ]