from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()
from Socket.serializers import UserSerializers
from rest_framework import viewsets,filters
from django_filters.rest_framework import DjangoFilterBackend



class UserViewSet(viewsets.ModelViewSet):
    queryset=User.objects.all().order_by('-date_joined')
    serializer_class=UserSerializers
    filter_backends = [filters.SearchFilter,filters.OrderingFilter,DjangoFilterBackend]
    search_fields = ('username', 'id', 'nickname')
    ordering_fields = ('username', 'id', 'nickname')
    filterset_fields = ('id','username',)

