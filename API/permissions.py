from rest_framework import permissions


class UserSafePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        return obj.id == request.user.id

class ProblemSetPermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return True
        #TODO: Add permissions