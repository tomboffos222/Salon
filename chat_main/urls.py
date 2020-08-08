from django.urls import path, include
from rest_framework import routers

from . import views
from rest_framework.authtoken import views as auth_view

urlpatterns = [

    path('users/', views.UserList.as_view(), name='user'),

    path('salons/', views.SalonsList.as_view(), name='salons'),
    path('salon/', views.SalonList.as_view(), name='salon'),
    path('profile', views.ProfileList.as_view(), name='profile'),
    path('obtain/token', auth_view.obtain_auth_token, name='get_token'),
    path('get/info', views.GetTokenUser.as_view(), name='get_user'),
    path('login', views.Login.as_view(), name='login'),
    path('login/check', views.CheckLogin.as_view(), name='login_check')
    # path('/user', views.UserMain.as_view(), name='user')
]
