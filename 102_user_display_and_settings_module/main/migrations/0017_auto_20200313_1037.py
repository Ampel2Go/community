# Generated by Django 2.1.1 on 2020-03-13 10:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0016_auto_20200313_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikiarticle',
            name='date',
            field=models.DateField(default=datetime.datetime(2020, 3, 13, 10, 37, 26, 731503)),
        ),
    ]