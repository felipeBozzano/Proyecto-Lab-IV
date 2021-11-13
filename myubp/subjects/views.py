from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from subjects.permissions import SubjectPermissions
from subjects.serializers import SubjectSerializer
from subjects.models import Subject
from users_degrees.models import UserDegree


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (SubjectPermissions,)

    def get_queryset(self):
        """
        Redefined the get query. User can only see their own degrees.
        """

        if not self.request.user.is_superuser:
            print("user: ", self.request.user)
            user_degree = UserDegree.objects.filter(id_user=self.request.user.id)
            for i in user_degree:
                print(i.id_degree)
            # print("user_degree: ", user_degree)
            return Response(status=status.HTTP_200_OK, data={"Status": "OK", "Message": "Note inserted"})
        return Subject.objects.all()
