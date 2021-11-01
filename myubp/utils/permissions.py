from rest_framework import permissions


class EditorPermissions(permissions.BasePermission):
    """
    Defined the permissions for normal and superusers
    """

    def has_permission(self, request, view):
        """
        Exclusive permissions for the superuser
        """

        allowed_methods = ['POST', 'PUT', 'PATCH']
        if not request.user.is_authenticated:
            return False
        if not request.user.is_superuser and request.method in allowed_methods:
            return False
        return True
