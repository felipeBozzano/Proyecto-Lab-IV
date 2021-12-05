from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from subjects.permissions import SubjectPermissions
from subjects.serializers import SubjectSerializer
from subjects.models import Subject
from users_degrees.models import UserDegree


class SubjectViewSet(viewsets.ModelViewSet):
    """
    list:
    ## All Subjects
    ***List all logged user's degree's subjects if the logged user is not super user, otherwise list all degree's subjects.***

    create:
    ## Add Subject
    ***Only the super user can create a new Subject.***

    ***To create a new Subject you need the following body: ***

    ```
        {
            "id_degree": 2,
            "subject_name": "Álgebra I",
            "semester": 1
        }
    ```
    """
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (SubjectPermissions,)

    def get_queryset(self):
        """
        Redefined the get query. User can only see their own degrees.
        """

        if self.request.user.is_superuser:
            return Subject.objects.all()

        # Get logged user's degrees.
        user_degrees = UserDegree.objects.filter(id_user=self.request.user)
        # append degree's names to a list
        degrees = []
        for user_degree in user_degrees:
            degrees.append(user_degree.id_degree)
        print("degrees: ", degrees)

        return Subject.objects.filter(id_degree__in=degrees)
