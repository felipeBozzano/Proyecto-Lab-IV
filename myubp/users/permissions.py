from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """
    Allows the user to update his own profile
    """

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is trying to update his own profile
        """

        allowed_methods = ['PUT', 'GET']

        if request.user.is_superuser:
            return True

        if request.method in allowed_methods:
            return obj.id == request.user.id
