from django.db import models
from users.models import UserProfile
from degrees.models import Degree


class UserDegree(models.Model):
    id_user = models.ForeignKey(UserProfile, on_delete=models.CASCADE, related_name='user')
    id_degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name='degree')
