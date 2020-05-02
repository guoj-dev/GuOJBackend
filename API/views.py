from rest_framework import viewsets, filters
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from API.serializers import *
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.exceptions import ErrorDetail, ValidationError
from rest_framework.decorators import permission_classes as permission_classed
import API.signals

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

    def get_queryset(self):
        return User.objects.filter(is_active=True)


class ProblemSetViewSet(viewsets.ModelViewSet):
    queryset = ProblemSet.objects.all()
    serializer_class = ProblemSetSerializers
    filter_backends = [filters.SearchFilter,
                       filters.OrderingFilter, DjangoFilterBackend]
    permission_classes = [ProblemSetPermissions]

    def perform_create(self, serializer):
        serializer.save(created_by=serializers.CurrentUserDefault())



class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializers
    filter_backends = [filters.SearchFilter,
                       filters.OrderingFilter, DjangoFilterBackend]
    permission_classes = []

    def retrieve(self, request, pk=None):
        problem = self.get_object()
        serializer = self.get_serializer(problem)
        return Response(serializer.data)


class NoticeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializers
    permission_classes = []

    def retrieve(self, request, pk=None):
        notice = self.get_object()
        serializer = self.get_serializer(notice)
        return Response(serializer.data)