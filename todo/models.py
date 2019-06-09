from django.db import models

# Create your models here.


class Task(models.Model):
    text = models.CharField(max_length=140)
    done = models.BooleanField(default=False)
