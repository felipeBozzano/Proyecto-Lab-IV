from rest_framework import serializers
from subjects.models import Subject


class SubjectSerializer(serializers.ModelSerializer):
    """
    Serializes a Note object
    """

    class Meta:
        model = Subject
        fields = ['id', 'id_career', 'signature_name', 'semester']
