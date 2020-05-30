from rest_framework import permissions


class UserSafePermissions(permissions.BasePermission):
    def has_permission(self,request,view):
        if view.action in ['create','destory']:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if view.action in ['update','partial_update'] and (obj.id == request.user.id or request.user.is_superuser):
            return True
        if request.method in permissions.SAFE_METHODS:
            return True
        return False


class ProblemSetPermissions(permissions.BasePermission):
    def has_permission(self,request,view):
        return True
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return request.user.is_staff or request.user is obj.owner or request.user.has_perm('ProblemSet.admin')


class ProblemPermissions(permissions.BasePermission):
    def has_permission(self,request,view):
        return True
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        return (request.user in obj.ProblemProviderUser.all() or request.user in obj.ProblemProviderGroup.Users.all()) and not request.method in {'CREATE'}

class NoticePermissions(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS or request.user.is_superuser:
            return True
        return False