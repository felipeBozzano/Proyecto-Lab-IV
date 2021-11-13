from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from notes.permissions import NotePermissions
from notes.serializers import NoteSerializer
from notes.models import Note
from subjects.models import Subject
from users_degrees.models import UserDegree
from users.models import UserProfile


class NoteViewSet(viewsets.ModelViewSet):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (NotePermissions,)

    def get_queryset(self):
        """
        Redefined the get query. User can only see their own degrees.
        """

        user = self.request.user
        if not user.is_superuser:
            print(Note.objects.filter(id_user=user.id))
            return Note.objects.filter(id_user=user.id)
        return Note.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Allows the user to insert a note
        """
        degree = Subject.objects.get(id=request.data["id_subject"])
        user_degree = UserDegree.objects.filter(id_user=request.data["id_user"])
        user = request.user

        if request.user.is_superuser:
            user = UserProfile.objects.get(id=request.data["id_user"])
        note = request.data["exam_note"]

        for i in user_degree:
            if degree.id_degree == i.id_degree:
                created = Note.objects.create(id_user=user, id_subject=degree, exam_note=note)
                created.save()
                return Response(status=status.HTTP_200_OK, data={"Status": "OK", "Message": "Note inserted"})
            break

        return Response(status=status.HTTP_400_BAD_REQUEST, data={"Status": "FAILED", "Message": "User not suscripted"})
