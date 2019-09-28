from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from Databases.models import Problem
from .permissions import *



class UserSerializers(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        depths = 1
        permission_classes=[permissions.IsAuthenticatedOrReadOnly, UserPermissions]