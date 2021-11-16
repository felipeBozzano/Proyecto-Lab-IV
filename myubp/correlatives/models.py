from django.db import models
from subjects.models import Subject


class Correlative(models.Model):
    id_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='base_subject')
    correlative_subject = models.ForeignKey(Subject, on_delete=models.CASCADE, related_name='correlative_subject')

    class Meta:
        unique_together = ('id_subject', 'correlative_subject')

    # def __str__(self):
    #     return self.correlative_subject
