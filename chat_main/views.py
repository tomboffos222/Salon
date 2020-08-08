from django.shortcuts import render
from django.contrib.auth.models import User, Group

from django.http import HttpResponse

from rest_framework import viewsets, permissions, status
from rest_framework.authtoken import models

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from chat_main.models import Salon, Profile
from chat_main.serializers import UserSerializer, SalonSerializer, ProfileSerializer, TokenSerializer, \
    UserProfileSerializer


class UserList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        users = User.objects.all()
        users = UserSerializer(users, many=True)
        return Response({"data": users.data}, status=status.HTTP_200_OK)

    def post(self, request):

        user = UserSerializer(data=request.data)

        if user.is_valid():

            user = User.objects.create(username=request.POST.get('username'), password=request.POST.get('password'))
            token = Token.objects.create(user=user)
            token = TokenSerializer(token, many=False)

            profile = Profile.objects.create(user=user)
            profile = ProfileSerializer(profile)

            return Response({"data": {"token": token.data, "profile": profile.data}}, status=status.HTTP_201_CREATED)

        else:
            return Response({"data": user.errors}, status=status.HTTP_400_BAD_REQUEST)


class SalonsList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        salons = Salon.objects.order_by('-rating').all()

        salons = SalonSerializer(salons, many=True)

        return Response({"data": salons.data}, status=status.HTTP_200_OK)

    def post(self, request):
        salon = SalonSerializer(data=request.data)

        if salon.is_valid():
            salon.save()
            return Response({"data": salon.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"data": salon.errors}, status=status.HTTP_400_BAD_REQUEST)


class SalonList(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        url = request.query_params['url']
        salon = Salon.objects.filter(url=url)
        if salon:

            salon = SalonSerializer(salon[0], many=False)

            return Response({"data": salon.data}, status=status.HTTP_200_OK)
        else:
            return Response({"data": "Not found"}, status=status.HTTP_404_NOT_FOUND)


class ProfileList(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        profile = ProfileSerializer(data=request.data)

        if profile.is_valid():
            profile.save()
            return Response({"data": profile.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"error": profile.errors}, status=status.HTTP_400_BAD_REQUEST)

    permission_classes = [permissions.AllowAny]

    def get(self, request):
        id = request.query_params['id']
        user = Profile.objects.filter(id=id)
        if user:
            user = ProfileSerializer(user[0], many=False)
            return Response({"data": user.data}, status=status.HTTP_200_OK)
        else:
            return Response({"data": "Not found"}, status=status.HTTP_404_NOT_FOUND)


class GetTokenUser(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        key = request.POST.get('key')
        token = models.Token.objects.filter(key=key)

        token = TokenSerializer(token[0], many=False)

        return Response({"data": token.data})


class Login(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username, password=password)

        if user:
            token = models.Token.objects.filter(user=user[0])
            token = TokenSerializer(token[0], many=False)
            return Response({"data": token.data}, status=status.HTTP_200_OK)
        else:
            return Response({"data": "not found"}, status=status.HTTP_404_NOT_FOUND)


class CheckLogin(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        username = request.POST.get('username')
        user = User.objects.filter(username=username)
        if user:
            return Response({"data": "Имя пользователя занято"}, status=status.HTTP_409_CONFLICT)
        else:
            return Response({"data": "not found"}, status=status.HTTP_200_OK)
