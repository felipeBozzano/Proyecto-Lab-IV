from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from correlatives.permissions import CorrelativePermissions
from correlatives.serializers import CorrelativeSerializer
from correlatives.models import Correlative
from users_degrees.models import UserDegree
from subjects.models import Subject


class CorrelativeViewSet(viewsets.ModelViewSet):
    """
    # Correlatives API
    list:
        ## All correlatives
        * list all user_degrees correlatives
    """
    queryset = Correlative.objects.all()
    serializer_class = CorrelativeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (CorrelativePermissions,)

    def get_queryset(self):
        """
        Redefined the get query. User can only see their own correlatives.
        """

        user = self.request.user

        if not user.is_superuser:
            # Obtenemos las carreras del usuario logueado
            user_degrees = UserDegree.objects.filter(id_user=user)

            # Obtenemos todas las materias de todas las carreras del usuario logueado
            all_subjects = Subject.objects.filter(id_degree__in=user_degrees.values_list('id_degree', flat=True))

            # Obtenemos toas las correlativas de las materias de la carrera del usuario
            print("subjects id: ", all_subjects.values_list('pk', flat=True))
            all_correlatives = Correlative.objects.filter(id_subject__in=all_subjects.values_list('pk', flat=True))

            return all_correlatives
        return Correlative.objects.all()
