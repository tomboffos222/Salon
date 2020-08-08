# Generated by Django 3.0.7 on 2020-07-05 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_main', '0007_auto_20200705_1234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='about',
            field=models.TextField(max_length=400, null=True, verbose_name='О пользователе'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=254, null=True, verbose_name='Почта'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='fio',
            field=models.TextField(null=True, verbose_name='ФИО пользователя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.TextField(null=True, verbose_name='Фото пользователя'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='phone',
            field=models.CharField(max_length=200, null=True, verbose_name='Номер телефона'),
        ),
    ]