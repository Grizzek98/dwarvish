from django.db import models

class Char(models.Model):
    english = models.CharField(max_length=3)
    dwarvish = models.CharField(max_length=6)