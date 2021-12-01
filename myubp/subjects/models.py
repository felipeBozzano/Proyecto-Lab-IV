from django.db import models
from degrees.models import Degree


class Subject(models.Model):
    id_degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name='belonging_degree')
    subject_name = models.CharField(max_length=50)
    semester = models.IntegerField()

    class Meta:
        unique_together = ('id_degree', 'subject_name')

    def __str__(self):
        return self.subject_name