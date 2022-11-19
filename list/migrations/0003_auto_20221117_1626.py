# Generated by Django 3.2.16 on 2022-11-17 16:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('list', '0002_itemextended'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, default='No Description', null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='favourite',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='item',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='urgent',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='list',
            name='list_owner',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='ItemExtended',
        ),
    ]