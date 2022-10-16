# Generated by Django 3.2.16 on 2022-10-16 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0005_auto_20221014_0651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='list',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(default='New List', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='list',
            name='slug',
            field=models.SlugField(default='New List', unique=True),
        ),
    ]