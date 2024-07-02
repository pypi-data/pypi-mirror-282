from django.db import models
from desmy_python.models import DesmyManager

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    objects = DesmyManager()

    def __str__(self):
        return self.name
