# Generated by Django 2.1.1 on 2020-04-09 18:35

from django.db import migrations, models
import django.utils.timezone
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0021_auto_20200313_1306'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewsArticle',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='title', max_length=100)),
                ('title_short', models.CharField(default='title_short', max_length=27)),
                ('body', tinymce.models.HTMLField(default='body')),
                ('date', models.DateField(default=django.utils.timezone.now)),
            ],
            options={
                'ordering': ['date'],
            },
        ),
        migrations.AlterModelOptions(
            name='wikiarticle',
            options={'ordering': ['chapter_id', 'subchapter_id', 'date']},
        ),
    ]
