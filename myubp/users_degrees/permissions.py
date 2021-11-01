from rest_framework import permissions

from users_degrees.models import UserDegree


class UserDegreePermissions(permissions.BasePermission):
    """
    Allows to each user ABM about their degrees
    """

    def has_permission(self, request, view):
        """
        Permissions for normal users
        """

        allowed_methods = ['POST', 'GET', 'DELETE']

        if not request.user.is_authenticated:
            return False
        if not request.user.is_superuser and request.method in allowed_methods:
            return False
        # COMO HACER PARA NO PERMITIR POST Y DELETE
        # CUANDO EL ID_USER DEL REQUEST NO ES EL MISMO QUE EL ID_USER DEL USER_DEGREE
        return True

    def has_object_permission(self, request, view, obj):
        """
        Check if the user is trying to update his own UserDegree
        """

        allowed_methods = ['GET', 'DELETE']

        if request.user.is_superuser:
            return True

        if request.method in allowed_methods:
            return obj.id_user == request.user.id
