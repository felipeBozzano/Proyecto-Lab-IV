from django.db import models
from degrees.models import Degree


class Subject(models.Model):
    id_career = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name='belonging_degree')
    signature_name = models.CharField(max_length=50, unique=True)
    semester = models.IntegerField()
