from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from users_degrees.permissions import UserDegreePermissions
from users_degrees.serializers import UserDegreeSerializer
from users_degrees.models import UserDegree


class UserDegreeViewSet(viewsets.ModelViewSet):
    queryset = UserDegree.objects.all()
    serializer_class = UserDegreeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (UserDegreePermissions,)

    def get_queryset(self):
        """
        Redefined the get query. User can only see their own degrees.
        """

        user = self.request.user
        if not user.is_superuser:
            return UserDegree.objects.filter(id_user=user.id)
        return UserDegree.objects.all()
