from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication

from utils.permissions import EditorPermissions
from degrees import serializers, models


class DegreeViewSet(viewsets.ModelViewSet):
    """
   list:
   ## All Degrees:
   ***List all degrees***

   create:
   ## New Degree
   ***Only the super user can create a new Degree
    To create a new Degree yoy need the following body:***

    ```
        {
            "name": "Ingenieria Informatica"
        }
    ```
   """
    queryset = models.Degree.objects.all()
    serializer_class = serializers.DegreeSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = [EditorPermissions]
