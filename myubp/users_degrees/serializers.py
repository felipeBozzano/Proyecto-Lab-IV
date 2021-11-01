from rest_framework import serializers
from users_degrees.models import UserDegree


class UserDegreeSerializer(serializers.ModelSerializer):
    """
    Serializes a UsersDegrees object
    """

    class Meta:
        model = UserDegree
        fields = ['id', 'id_user', 'id_degree']
