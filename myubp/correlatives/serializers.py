from rest_framework import serializers
from correlatives.models import Correlative


class CorrelativeSerializer(serializers.ModelSerializer):
    """
    Serializes a Note object
    """

    # serialize id_subject and correlative_subject with __str__ class method
    id_subject = serializers.StringRelatedField()
    correlative_subject = serializers.StringRelatedField()

    class Meta:
        model = Correlative
        fields = ['id', 'id_subject', 'correlative_subject']
