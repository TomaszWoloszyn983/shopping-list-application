# Generated by Django 3.2.16 on 2022-10-07 06:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0002_auto_20221007_0633'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AddField(
            model_name='item',
            name='slug',
            field=models.SlugField(default='', unique=True),
        ),
    ]