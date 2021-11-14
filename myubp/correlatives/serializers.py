from rest_framework import serializers
from correlatives.models import Correlative


class CorrelativeSerializer(serializers.ModelSerializer):
    """
    Serializes a Note object
    """

    # serializamos los id por sus to_string
    id_subject = serializers.StringRelatedField()
    correlative_subject = serializers.StringRelatedField()

    class Meta:
        model = Correlative
        fields = ['id', 'id_subject', 'correlative_subject']
