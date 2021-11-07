from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from notes.permissions import NotePermissions
from notes.serializers import NoteSerializer
from notes.models import Note


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
            return Note.objects.filter(id_user=user.id)
        return Note.objects.all()

    '''
    def create(self, request, *args, **kwargs):
        """
        Allows the user to insert a note
        """
        #user = request.user
        print(request.data)
        return False
        #created = Cart.objects.create(user=user)
        #created.save()
        #return Response(status=status.HTTP_200_OK, data={"Status": "OK", "Message": "Carrito creado con exito"})
    '''
