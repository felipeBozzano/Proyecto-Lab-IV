from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from correlatives.permissions import CorrelativePermissions
from correlatives.serializers import CorrelativeSerializer
from correlatives.models import Correlative


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
        if not user.is_superuser:
            return Correlative.objects.filter(id_user=user.id)
        return Correlative.objects.all()
