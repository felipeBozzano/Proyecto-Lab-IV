from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from users_degrees.permissions import UserDegreePermissions
from users_degrees.serializers import UserDegreeSerializer
from users_degrees.models import UserDegree


class UserDegreeViewSet(viewsets.ModelViewSet):
    """
    # UserDegree API
    list:
    ## All UserDegree
    ***If the logged user is superuser then list al UserDegree. Otherwise list logged user's UserDegree***

    create:
    ## Create UserDegree
    ***Allows to create a new UserDegree.
    You will need the following body: ***

    ```
        {
            "id_user": 4,
            "id_degree": 1
        }
    ```
    """
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
