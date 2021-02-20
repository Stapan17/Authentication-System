from django.db import models
from django.contrib.auth.models import User


class infoUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=25)
    profile_picture = models.ImageField(
        upload_to='profile_picture', blank=True, null=True)

    def __str__(self):
        return self.name
