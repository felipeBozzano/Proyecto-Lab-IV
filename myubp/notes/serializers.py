from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializes a Note object
    """

    class Meta:
        model = Note
        fields = ['id', 'id_user', 'id_subject', 'exam_note']


class AvgSerializer(serializers.ModelSerializer):
    """
    Serializes a notes AVG
    """

    average_note = serializers.SerializerMethodField()

    @staticmethod
    def get_average_note(obj):
        return obj['_average_note']

    class Meta:
        model = Note
        fields = ['average_note', 'id_user_id']
