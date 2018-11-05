from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_object_permission(self, request, view, obj):

        return (request.user and request.user.is_superuser) or (
            obj.user == request.user)


class IsAdminUserOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """

    def has_permission(self, request, view):

        return request.user and request.user.is_staff


class IsSameUserAllowEditionOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    """
    def has_permission(self, request, view):

        # grant permission only if the method is the PUT method
        return request.user.is_staff or request.method == 'PUT'

    def has_object_permission(self, request, view, obj):

        return request.user.is_staff or (request.method == 'PUT' and
                                         obj.id == request.user.id)
