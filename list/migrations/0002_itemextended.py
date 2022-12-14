# Generated by Django 3.2.16 on 2022-11-04 07:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ItemExtended',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=50, unique=True)),
                ('slug', models.SlugField(default='', unique=True)),
                ('quantity', models.CharField(default='1', max_length=5)),
                ('bought', models.BooleanField(default=False)),
                ('favourite', models.BooleanField(default=False)),
                ('urgent', models.BooleanField(default=False)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
                ('description', models.TextField(blank=True, default='No Description', null=True)),
                ('list_name', models.ForeignKey(default='None', on_delete=django.db.models.deletion.CASCADE, related_name='itemsextended', to='list.list')),
            ],
            options={
                'ordering': ['-bought'],
            },
        ),
    ]
