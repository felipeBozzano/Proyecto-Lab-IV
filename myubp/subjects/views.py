from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

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

        if self.request.user.is_superuser:
            return Subject.objects.all()

        # Obtenemos las carreras del usuario logueado
        user_degrees = UserDegree.objects.filter(id_user=self.request.user)
        # Agregamos los degrees_name en una lista
        degrees = []
        for user_degree in user_degrees:
            degrees.append(user_degree.id_degree)
        print("degrees: ", degrees)

        return Subject.objects.filter(id_degree__in=degrees)

        # Obtenemos todas las materias de todas las carreras del usuario logueado
        # subjects = []
        # all_subjects = Subject.objects.filter(id_degree__in=degrees)
        # for subject in all_subjects:
            # subjects.append(subject.id)
        # print("subjects: ", subjects)

        """if not self.request.user.is_superuser:
            print("user: ", self.request.user)
            user_degree = UserDegree.objects.filter(id_user=self.request.user.id)
            id_degrees = []
            for i in user_degree:
                id_degrees.append(i.id_degree)
            return Subject.objects.filter(id_degree__in=id_degrees)
        return Subject.objects.all()"""
