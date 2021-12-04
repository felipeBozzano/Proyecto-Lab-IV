from django.db.models import Avg
from rest_framework import viewsets, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response

from notes.permissions import NotePermissions
from notes.serializers import NoteSerializer, AvgSerializer
from notes.models import Note
from subjects.models import Subject
from users_degrees.models import UserDegree
from users.models import UserProfile


class NoteViewSet(viewsets.ModelViewSet):
    """
        # Notes API
        list:
            ## All Notes
            ***List all logged user's exam notes if the logged user is not super user, otherwise list all exam notes.***

        create:
            ## Add Note
            ****Allows the user to add notes to the subjects of his degrees. The user is not allowed to add notes
             to degree's subjects in which he does not belong.
             To create a new note you will need the following body: ****
             ```
                {
                    "id_user": 2,
                    "id_subject": 5,
                    "exam_note": 6
                }
             ```
    """
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (NotePermissions,)

    def get_queryset(self):
        """
        Redefined the get query. User can only see their own notes.
        """

        # Every normal user obtains only their notes
        user = self.request.user
        if not user.is_superuser:
            return Note.objects.filter(id_user=user.id)
        return Note.objects.all()

    def create(self, request, *args, **kwargs):
        """
        Allows the user to insert a note
        """

        # get the degree of the subject and the user_degrees of the user.
        degree = Subject.objects.get(id=request.data["id_subject"])
        user_degree = UserDegree.objects.filter(id_user=request.data["id_user"])
        user = request.user

        # superuser can obtain all registers of any user.
        if request.user.is_superuser:
            user = UserProfile.objects.get(id=request.data["id_user"])

        # get the note of the exam
        note = request.data["exam_note"]

        # if the degree of the subject matches with any degree in the user_degrees registers, create the note
        for i in user_degree:
            if degree.id_degree == i.id_degree:
                created = Note.objects.create(id_user=user, id_subject=degree, exam_note=note)
                created.save()
                return Response(status=status.HTTP_200_OK, data={"Status": "OK", "Message": "Note inserted"})

        return Response(status=status.HTTP_400_BAD_REQUEST, data={"Status": "FAILED", "Message": "User not suscripted"})


class AvgNoteViewSet(viewsets.ModelViewSet):
    """
        # Note AVG API
        list:
            ## Average exam note
            ***Return exam note's average for logged user. If the logged user is a root user, he can se all the
             exam note's average***
    """
    serializer_class = AvgSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (NotePermissions,)

    def get_queryset(self):
        user = self.request.user
        print("user: ", user)
        if not user.is_superuser:
            return Note.objects.select_related('subjects').filter(id_user_id=user).values('id_user_id') \
                .annotate(_average_note=Avg('exam_note'))
        return Note.objects.all().values('id_user_id', 'id_degree_id').annotate(_average_note=Avg('exam_note'))
