from rest_framework import viewsets, filters
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from API.serializers import *
from django.shortcuts import render
from django.contrib.auth import get_user_model
User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializers
    filter_backends = [filters.SearchFilter,
                       filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ('username', 'id', 'nickname')
    ordering_fields = ('username', 'id', 'nickname')
    filterset_fields = ('id', 'username',)
    permission_classes = (UserUpdatePermissions,UserSafePermissions)