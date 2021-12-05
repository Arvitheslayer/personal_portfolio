from django.db import models

class All_blogs(models.Model):
    title = models.CharField(max_length=200)
    date = models.DateTimeField()
    description = models.TextField()

    def __str__(self):
        return self.title