from django.contrib.auth.models import User
from django.db import models


# Create your models here.


class Profile(models.Model):
    fio = models.TextField(verbose_name='ФИО пользователя', null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    about = models.TextField(max_length=400, verbose_name='О пользователе', null=True)
    email = models.EmailField(verbose_name='Почта', null=True)
    phone = models.CharField(max_length=200, verbose_name='Номер телефона', null=True)
    image = models.TextField(verbose_name='Фото пользователя', null=True)
    birthday = models.DateField(null=True)
    last_login = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания профиля')


class Salon(models.Model):
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name="Администратор", blank=True,
                              related_name='admin')
    avatar = models.TextField(verbose_name="Фото салона", null=True)
    title = models.CharField(max_length=255, verbose_name="Название салона", null=True)
    city = models.CharField(max_length=255, verbose_name="Город", null=True)
    main_background = models.TextField(verbose_name="Задний фон", null=True)
    address = models.CharField(max_length=255, verbose_name="Адрес салона", null=True)
    url = models.CharField(max_length=255, verbose_name="Ссылка на страницу салона", null=True)
    rating = models.FloatField(verbose_name="Рейтинг салона", default=0)
    subscribers = models.BigIntegerField(verbose_name="Количество подписчиков", default=0)
    masters = models.IntegerField(verbose_name="Количество мастеров", default=0, )
    deals = models.IntegerField(verbose_name="Количество предоставленных услуг", default=0)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания аккаунта салона')


class Master(models.Model):
    profile = models.OneToOneField(Profile, on_delete=models.CASCADE, verbose_name="Профиль")
    avatar = models.TextField(verbose_name="Аватар мастера")
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name="Салон в котором работает", blank=True,
                              related_name='workers')

    deals = models.IntegerField(verbose_name="Количество предоставленных услуг", default=0)
    about = models.TextField(verbose_name="О мастере")
    rating = models.FloatField(verbose_name="Рейтинг мастера", default=0)
    subscribers = models.BigIntegerField(verbose_name="Количество подписчиков", default=0)
    work_types = models.TextChoices('WorkType', 'FREELANCE SALON')
    percent_from_work = models.IntegerField(null=True)
    work_type = models.CharField(choices=work_types.choices, verbose_name='Вид деятельности', default='FREELANCE',
                                 max_length=200)
    master_of = models.TextField(verbose_name='Умения', default='Пока пусто')
    experience = models.IntegerField(verbose_name='Опыт работы', default=0)
    levels = models.TextChoices('Levels', 'TEACHER_TOP_MASTER TOP_MASTER MASTER BEGINNING')
    level = models.TextField(verbose_name='Уровень мастера', default='BEGINNING', choices=levels.choices,
                             max_length=300)
    crated_at = models.DateField(auto_now=True, verbose_name="Дата создания аккаунта мастера")


class Price(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Создатель цены", null=True, blank=True,
                               related_name='master_prices')
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name="Салон", null=True, blank=True,
                              related_name='salon_prices')
    salon_masters = models.ManyToManyField(Master, verbose_name="Мастера салона", null=True, blank=True,
                                           related_name='salon_masters')
    price = models.BigIntegerField(verbose_name='Цена услуги', default=0)
    title = models.TextField(verbose_name='Название услуги')
    average_time = models.IntegerField(verbose_name='Среднее время услуги', default=0)
    discount_price = models.BigIntegerField(verbose_name='Скидочная цена', default=0)
    description = models.TextField(verbose_name='Описание услуги', null=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')


class Post(models.Model):
    master = models.ForeignKey(Master, on_delete=models.CASCADE, verbose_name="Создатель поста", null=True,
                               related_name='master_posts', blank=True)
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name="Пост Салона", null=True,
                              related_name='salon_posts', blank=True)

    title = models.TextField(verbose_name='Название поста')
    description = models.TextField(verbose_name='Описание поста', null=True)
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания')


class MediaContent(models.Model):
    price_link = models.ForeignKey(Price, on_delete=models.CASCADE, verbose_name='Услуга', related_name='price_medias',
                                   blank=True, null=True, )
    post_link = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='post_medias',
                                  blank=True, null=True)

    on_main = models.BooleanField(default=False)
    media_link = models.TextField(verbose_name='Ссылка на медиа контент')
    created_at = models.DateTimeField(auto_now=True, verbose_name='Дата создания фото')


class Order(models.Model):
    price = models.ForeignKey(Price, on_delete=models.CASCADE, verbose_name='Услуга', related_name='prices')
    client = models.ForeignKey(Profile, on_delete=models.CASCADE, verbose_name='Клиент', related_name='client')
    master = models.ManyToManyField(Master, verbose_name='Исполнители', related_name='masters')
    salon = models.ForeignKey(Salon, on_delete=models.CASCADE, verbose_name='Салон исполнителя', related_name='salon',
                              null=True)
    start_time = models.DateTimeField(verbose_name='Дата записи')
    end_time = models.DateTimeField(verbose_name='Дата окончания')
