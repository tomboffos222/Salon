# Generated by Django 3.0.7 on 2020-06-29 19:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Master',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.TextField(verbose_name='Аватар мастера')),
                ('deals', models.IntegerField(default=0, verbose_name='Количество предоставленных услуг')),
                ('about', models.TextField(verbose_name='О мастере')),
                ('rating', models.FloatField(default=0, verbose_name='Рейтинг мастера')),
                ('subscribers', models.BigIntegerField(default=0, verbose_name='Количество подписчиков')),
                ('work_type', models.CharField(choices=[('FREELANCE', 'Freelance'), ('SALON', 'Salon')], default='FREELANCE', max_length=200, verbose_name='Вид деятельности')),
                ('master_of', models.TextField(default='Пока пусто', verbose_name='Умения')),
                ('experience', models.IntegerField(default=0, verbose_name='Опыт работы')),
                ('level', models.TextField(choices=[('TEACHER_TOP_MASTER', 'Teacher Top Master'), ('TOP_MASTER', 'Top Master'), ('MASTER', 'Master'), ('BEGINNING', 'Beginning')], default='BEGINNING', max_length=300, verbose_name='Уровень мастера')),
                ('crated_at', models.DateField(auto_now=True, verbose_name='Дата создания аккаунта мастера')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fio', models.TextField(verbose_name='ФИО пользователя')),
                ('about', models.TextField(max_length=400, verbose_name='О пользователе')),
                ('email', models.EmailField(max_length=254, verbose_name='Почта')),
                ('phone', models.CharField(max_length=200, verbose_name='Номер телефона')),
                ('image', models.TextField(verbose_name='Фото пользователя')),
                ('birthday', models.DateField()),
                ('last_login', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания профиля')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Salon',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.TextField(verbose_name='Фото салона')),
                ('title', models.CharField(max_length=255, verbose_name='Название салона')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес салона')),
                ('url', models.CharField(max_length=255, verbose_name='Ссылка на страницу салона')),
                ('rating', models.FloatField(default=0, verbose_name='Рейтинг салона')),
                ('subscribers', models.BigIntegerField(default=0, verbose_name='Количество подписчиков')),
                ('masters', models.IntegerField(default=0, verbose_name='Количество мастеров')),
                ('deals', models.IntegerField(default=0, verbose_name='Количество предоставленных услуг')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания аккаунта салона')),
                ('admin', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='admin', to='chat_main.Profile', verbose_name='Администратор')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.BigIntegerField(default=0, verbose_name='Цена услуги')),
                ('title', models.TextField(verbose_name='Название услуги')),
                ('discount_price', models.BigIntegerField(default=0, verbose_name='Скидочная цена')),
                ('description', models.TextField(null=True, verbose_name='Описание услуги')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('master', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat_main.Master', verbose_name='Создатель цены')),
                ('salon', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat_main.Salon', verbose_name='Салон')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Название поста')),
                ('description', models.TextField(null=True, verbose_name='Описание поста')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания')),
                ('master', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat_main.Master', verbose_name='Создатель поста')),
                ('salon', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='chat_main.Salon', verbose_name='Пост Салона')),
            ],
        ),
        migrations.CreateModel(
            name='MediaContent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('on_main', models.BooleanField(default=False)),
                ('media_link', models.TextField(verbose_name='Ссылка на медиа контент')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Дата создания фото')),
                ('post_link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='chat_main.Post', verbose_name='Пост')),
                ('price_link', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='prices', to='chat_main.Price', verbose_name='Услуга')),
            ],
        ),
        migrations.AddField(
            model_name='master',
            name='profile',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chat_main.Profile', verbose_name='Профиль'),
        ),
        migrations.AddField(
            model_name='master',
            name='salon',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='workers', to='chat_main.Salon', verbose_name='Салон в котором работает'),
        ),
    ]
