from rest_framework import viewsets, filters
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from API.serializers import *
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets,mixins
from rest_framework.response import Response
from rest_framework.exceptions import ErrorDetail, ValidationError

User = get_user_model()


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserDataSerializers
    filter_backends = [filters.SearchFilter,
                       filters.OrderingFilter, DjangoFilterBackend]
    search_fields = ('username', 'id')
    ordering_fields = ('username', 'id')
    filterset_fields = ('id', 'username')
    permission_classes = (UserSafePermissions,)

    def retrieve(self, request, pk=None):
        user = self.get_object()
        serializer = self.get_serializer(user)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({'detail':'您没有执行该操作的权限。'})

    def destroy(self, request, *args, **kwargs):
        return Response({'detail':'您没有执行该操作的权限。'})