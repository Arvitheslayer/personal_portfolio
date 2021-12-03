from django.db import models

class All_blogs(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField()
    description = models.CharField(max_length=250)
