from django.db import models

class Lesson(models.model):
    title = models.DateField()
    desciption = models.CharField()