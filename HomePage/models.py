from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Link(models.Model):
    url = models.URLField()
    visitors = models.IntegerField(default=0)
    is_active = models.BooleanField(default=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.url
