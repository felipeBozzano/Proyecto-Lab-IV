from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from correlatives.permissions import CorrelativePermissions
from correlatives.serializers import CorrelativeSerializer
from correlatives.models import Correlative
from users_degrees.models import UserDegree
from subjects.models import Subject


class CorrelativeViewSet(viewsets.ModelViewSet):
    queryset = Correlative.objects.all()
    serializer_class = CorrelativeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (CorrelativePermissions,)

    def get_queryset(self):
        """
        Redefined the get query. User can only see their own correlatives.
        """

        user = self.request.user
        print("user: ", user)

        if not user.is_superuser:
            # Obtenemos las carreras del usuario logueado
            user_degrees = UserDegree.objects.filter(id_user=user.id)
            # Agregamos los degrees_name en una lista
            degrees = []
            for user_degree in user_degrees:
                degrees.append(user_degree.id_degree)
            print("degrees: ", degrees)

            # Obtenemos todas las materias de todas las carreras del usuario logueado
            subjects = []
            all_subjects = Subject.objects.filter(id_degree__in=degrees)
            for subject in all_subjects:
                subjects.append(subject.id)
            print("subjects: ", subjects)

            # Obtengo todas las correlativas de todas las materias del usuario logueado
            correlatives = []
            all_correlatives = Correlative.objects.filter(id_subject__in=subjects)
            for correlative in all_correlatives:
                correlatives.append(correlative)
            return correlatives
        return Correlative.objects.all()
