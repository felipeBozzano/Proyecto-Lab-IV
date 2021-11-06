from rest_framework import serializers
from correlatives.models import Correlative


class CorrelativeSerializer(serializers.ModelSerializer):
    """
    Serializes a Note object
    """

    class Meta:
        model = Correlative
        fields = ['id', 'id_subject', 'correlative_subject']
