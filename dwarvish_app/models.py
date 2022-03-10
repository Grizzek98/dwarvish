from django.db import models

class Lesson(models.Model):
    title = models.DateField()
    description = models.TextField()