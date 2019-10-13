from rest_framework import permissions


class UserSafePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser:
            return True
        return False

class UserUpdatePermissions(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        if request.user.is_superuser or view.action!='create':
            return True
        return False