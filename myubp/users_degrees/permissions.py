from rest_framework import permissions
from users.models import UserProfile


class UserDegreePermissions(permissions.BasePermission):
    """
    Allows to each user ABM about their degrees
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
        Check if the user is trying to update his own UserDegree
        """

        if not request.user.is_authenticated:
            return False
        if not request.user.is_superuser:
            return UserProfile.objects.get(email=obj.id_user).id == request.user.id
        return True
