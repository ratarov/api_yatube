from rest_framework import permissions


class isAuthorOrAuthenticated(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in ('GET', 'POST'):
            return request.user.is_authenticated
        if request.method in ('PATCH', 'PUT', 'DELETE'):
            return request.user.is_authenticated and obj.author == request.user
