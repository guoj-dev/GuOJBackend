from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()
from Socket.serializers import UserSerializers
from rest_framework import viewsets



class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class=UserSerializers

