from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from correlatives.permissions import CorrelativePermissions
from correlatives.serializers import CorrelativeSerializer
from correlatives.models import Correlative
from users_degrees.models import UserDegree
from subjects.models import Subject
from rest_framework.response import Response
from rest_framework import status


class CorrelativeViewSet(viewsets.ModelViewSet):
    """
    list:
    ### All correlatives:
    ***List all user's degrees correlatives***

    create:
    ### New Correlative:
    ***Only the super user can create a new Correlative
    To create a new Degree you need the following body:***

    ```
        {
            "id_subject": 8,
            "correlative_subject": 9
        }
    ```
    """
    queryset = Correlative.objects.all()
    serializer_class = CorrelativeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (CorrelativePermissions,)

    def get_queryset(self):
        """
        Redefined the get queryset. No super user can only see their own correlatives. And superuser can see all
        correlatives
        """

        user = self.request.user

        if not user.is_superuser:
            # get logged user's degrees
            user_degrees = UserDegree.objects.filter(id_user=user)

            # get logged users degree's subjects
            all_subjects = Subject.objects.filter(id_degree__in=user_degrees.values_list('id_degree', flat=True))

            # get subject's correlatives
            print("subjects id: ", all_subjects.values_list('pk', flat=True))
            all_correlatives = Correlative.objects.filter(id_subject__in=all_subjects.values_list('pk', flat=True))

            return all_correlatives
        return Correlative.objects.all()

    def create(self, request, *args, **kwargs):
        id_subject = request.data["id_subject"]
        subject = Subject.objects.get(id=id_subject)
        correlative_subject = request.data["correlative_subject"]
        correlative = Subject.objects.get(id=correlative_subject)

        Correlative.objects.create(id_subject=subject, correlative_subject=correlative).save()

        return Response(status=status.HTTP_200_OK, data={"Status": "OK", "Message": "Correlative inserted"})
