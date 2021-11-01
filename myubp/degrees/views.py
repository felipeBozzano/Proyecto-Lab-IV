from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from utils.permissions import EditorPermissions
from degrees import serializers, models


class DegreeViewSet(viewsets.ModelViewSet):
    queryset = models.Degree.objects.all()
    serializer_class = serializers.DegreeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [EditorPermissions]
