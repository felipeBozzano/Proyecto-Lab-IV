from rest_framework import permissions
from users.models import UserProfile


class NotePermissions(permissions.BasePermission):
    """
    Allows to each user ABM about their notes
    """

    def has_permission(self, request, view):
        """
        Permissions for normal users
        """

        if not request.user.is_authenticated:
            return False
        return True

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is trying to update his own Note
        """

        allowed_methods = ['GET', 'PUT', 'DELETE']

        if not request.user.is_authenticated:
            return False
        if request.user.is_superuser:
            return True
        if request.method in allowed_methods:
            return obj.id_user == UserProfile.objects.get(id=request.user.id)
