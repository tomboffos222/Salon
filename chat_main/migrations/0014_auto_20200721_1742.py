# Generated by Django 3.0.7 on 2020-07-21 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_main', '0013_master_background'),
    ]

    operations = [
        migrations.AlterField(
            model_name='master',
            name='background',
            field=models.TextField(default=0, verbose_name='Задний фон'),
        ),
    ]