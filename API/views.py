from rest_framework import viewsets, filters
from .permissions import *
from django_filters.rest_framework import DjangoFilterBackend
from API.serializers import *
from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework import viewsets, mixins
from rest_framework.response import Response
from rest_framework.exceptions import ErrorDetail, ValidationError
from rest_framework.decorators import permission_classes as permission_classed, action
import API.signals
from guardian.shortcuts import assign_perm, remove_perm

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

    @action(method=['post'], detail=True)
    def authorize(self, request, pk):
        this_object = ProblemSet.objects.get(pk=pk)
        if (request.user.is_authenticated() and request.user.has_perm('ProblemSet.admin', this_object)) or request.user.is_staff:
            if request.data.view:
                assign_perm('view', User.objects.get(request.data.userid), this_object)
            if request.data.create:
                assign_perm('create', User.objects.get(request.data.userid), this_object)
            if request.data.update:
                assign_perm('update', User.objects.get(request.data.userid), this_object)
            if request.data.admin:
                assign_perm('admin', User.objects.get(request.data.userid), this_object)
        else:
            self.permission_denied(request, "Unauthorized Action")

    @action(method=['post'], detail=True)
    def disauth(self, request, pk):
        this_object = ProblemSet.objects.get(pk=pk)
        if (request.user.is_authenticated() and request.user.has_perm('ProblemSet.admin', this_object)) or request.user.is_staff:
            if request.data.view:
                remove_perm('view', User.objects.get(request.data.userid), this_object)
            if request.data.create:
                remove_perm('create', User.objects.get(request.data.userid), this_object)
            if request.data.update:
                remove_perm('update', User.objects.get(request.data.userid), this_object)
            if request.data.admin:
                remove_perm('admin', User.objects.get(request.data.userid), this_object)
        else:
            self.permission_denied(request, "Unauthorized Action")


class ProblemViewSet(viewsets.ModelViewSet):
    queryset = Problem.objects.all()
    serializer_class = ProblemSerializers
    filter_backends = [filters.SearchFilter,
                       filters.OrderingFilter, DjangoFilterBackend]
    permission_classes = []

    @action(method=['post'], detail=True)
    def authorize(self, request, pk):
        this_object = Problem.objects.get(pk=pk)
        if (request.user.is_authenticated() and request.user.has_perm('Problem.admin', this_object)) or request.user.is_staff:
            if request.data.view:
                assign_perm('view', User.objects.get(request.data.userid), this_object)
            if request.data.create:
                assign_perm('create', User.objects.get(request.data.userid), this_object)
            if request.data.update:
                assign_perm('update', User.objects.get(request.data.userid), this_object)
            if request.data.admin:
                assign_perm('admin', User.objects.get(request.data.userid), this_object)
        else:
            self.permission_denied(request, "Unauthorized Action")

    @action(method=['post'], detail=True)
    def disauth(self, request, pk):
        this_object = Problem.objects.get(pk=pk)
        if (request.user.is_authenticated() and request.user.has_perm('Problem.admin', this_object)) or request.user.is_staff:
            if request.data.view:
                remove_perm('view', User.objects.get(request.data.userid), this_object)
            if request.data.create:
                remove_perm('create', User.objects.get(request.data.userid), this_object)
            if request.data.update:
                remove_perm('update', User.objects.get(request.data.userid), this_object)
            if request.data.admin:
                remove_perm('admin', User.objects.get(request.data.userid), this_object)
        else:
            self.permission_denied(request, "Unauthorized Action")

class NoticeViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Notice.objects.all()
    serializer_class = NoticeSerializers
    permission_classes = []
