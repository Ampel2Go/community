# Generated by Django 2.1.1 on 2020-05-29 00:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0028_auto_20200528_2005'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occupancy',
            name='direction',
            field=models.BooleanField(default=False),
        ),
    ]