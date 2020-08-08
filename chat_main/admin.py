from django.contrib import admin

# Register your models here.
from .models import Salon, Profile, Master, Price, Post, MediaContent, Order

admin.site.register(Salon)
admin.site.register(Profile)
admin.site.register(Master)
admin.site.register(Price)
admin.site.register(Post)
admin.site.register(MediaContent)
admin.site.register(Order)
