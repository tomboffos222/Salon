# Generated by Django 3.0.7 on 2020-08-01 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_main', '0021_price_salon_masters'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='price',
            name='salon_masters',
        ),
        migrations.AddField(
            model_name='price',
            name='salon_masters',
            field=models.ManyToManyField(blank=True, null=True, related_name='salon_masters', to='chat_main.Master', verbose_name='Мастера салона'),
        ),
    ]
