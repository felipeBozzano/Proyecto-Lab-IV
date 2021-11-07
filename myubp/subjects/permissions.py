from rest_framework import permissions


class SubjectPermissions(permissions.BasePermission):
    """
    Allows to each user ABM about their subject
    """

    def has_permission(self, request, view):
        """
        Permissions for normal users
        """

        allowed_methods = ['GET']

        if not request.user.is_authenticated:
            return False
        if not request.user.is_superuser and request.method in allowed_methods:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is trying to update his own Note
        """

        allowed_methods = ['GET']

        if not request.user.is_authenticated:
            return False
        if not request.user.is_superuser and request.method in allowed_methods:
            return False
        return True
