from django.db import models
from django.db.models import Avg
from users.models import UserProfile
from subjects.models import Subject


class Note(models.Model):
    id_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user_note')
    id_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='subject_note')
    exam_note = models.IntegerField()

    @property
    def average_note(self):
        print("avg: ", Note.objects.aggregate(Avg('exam_note')))
        return Note.objects.aggregate(Avg('exam_note'))
