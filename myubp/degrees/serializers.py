from rest_framework import serializers
from degrees.models import Degree


class DegreeSerializer(serializers.ModelSerializer):
    """
    Serializes a Degree object
    """

    class Meta:
        model = Degree
        fields = ['id', 'name', 'approval_note']
