# Generated by Django 3.2.16 on 2022-10-14 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20221007_0648'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=('New List', 'Oct-14-2022'), max_length=50, unique=True)),
                ('slug', models.CharField(default=('New List', 'Oct-14-2022'), max_length=50, unique=True)),
            ],
        ),
    ]
