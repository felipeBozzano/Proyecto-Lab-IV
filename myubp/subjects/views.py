from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from subjects.permissions import SubjectPermissions
from subjects.serializers import SubjectSerializer
from subjects.models import Subject


class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (SubjectPermissions,)

    def get_queryset(self):
        """
        Redefined the get query. User can only see their own degrees.
        """

        user = self.request.user
        if not user.is_superuser:
            return Subject.objects.filter(id_user=user.id)
        return Subject.objects.all()
