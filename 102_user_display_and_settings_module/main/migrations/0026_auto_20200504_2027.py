# Generated by Django 2.1.1 on 2020-05-04 20:27

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_auto_20200502_2128'),
    ]

    operations = [
        migrations.CreateModel(
            name='Occupancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('capacity', models.IntegerField()),
                ('person_count', models.IntegerField(default=3)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.DeleteModel(
            name='SettingsModel',
        ),
    ]