from rest_framework import serializers
from notes.models import Note


class NoteSerializer(serializers.ModelSerializer):
    """
    Serializes a Note object
    """

    class Meta:
        model = Note
        fields = ['id', 'id_user', 'id_subject', 'exam_note']
