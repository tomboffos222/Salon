# Generated by Django 3.0.7 on 2020-07-05 18:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_main', '0009_price_average_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='master',
            name='percent_from_work',
            field=models.IntegerField(null=True),
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_time', models.DateTimeField(verbose_name='Дата записи')),
                ('end_time', models.DateTimeField(verbose_name='Дата окончания')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to='chat_main.Profile', verbose_name='Клиент')),
                ('master', models.ManyToManyField(null=True, related_name='masters', to='chat_main.Master', verbose_name='Исполнители')),
                ('price', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='chat_main.Price', verbose_name='Услуга')),
                ('salon', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='salon', to='chat_main.Salon', verbose_name='Салон исполнителя')),
            ],
        ),
    ]
