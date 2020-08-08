from django.contrib.auth.models import User
from rest_framework import serializers

from chat_main.models import Salon, Profile, Master, Price, MediaContent, Post
from rest_framework.authtoken import models


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password']


class ProfileSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = '__all__'


class MasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Master
        fields = '__all__'


class MediaContentSerializer(serializers.ModelSerializer):
    class Meta:
        model = MediaContent
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    post_medias = MediaContentSerializer(many=True)

    class Meta:
        model = Post
        fields = '__all__'


class PriceSerializer(serializers.ModelSerializer):
    price_medias = MediaContentSerializer(many=True)
    salon_masters = MasterSerializer(many=True)
    class Meta:
        model = Price
        fields = '__all__'


class SalonSerializer(serializers.ModelSerializer):
    workers = MasterSerializer(many=True)
    admin = ProfileSerializer(many=False)
    salon_prices = PriceSerializer(many=True)
    salon_posts = PostSerializer(many=True)


    class Meta:
        model = Salon

        fields = '__all__'


class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer(many=False)

    class Meta:
        model = models.Token
        fields = '__all__'


class UserProfileSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = User
        fields = '__all__'
