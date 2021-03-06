# Generated by Django 3.0.7 on 2020-07-26 17:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_main', '0018_auto_20200721_1828'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='master',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='master_posts', to='chat_main.Master', verbose_name='Создатель поста'),
        ),
        migrations.AlterField(
            model_name='post',
            name='salon',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salon_posts', to='chat_main.Salon', verbose_name='Пост Салона'),
        ),
    ]
