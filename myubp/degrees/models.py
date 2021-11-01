from django.db import models


class Degree(models.Model):
    name = models.CharField(max_length=50, unique=True)
    approval_note = models.IntegerField(default=4)

    def __str__(self):
        return self.name
