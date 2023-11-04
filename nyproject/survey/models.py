from django.db import models

class Survey(models.Model):
    name = models.CharField(default=0, max_length=255)
    neis = models.CharField(default=0, max_length=4)
    career = models.IntegerField(default=0)
    department = models.IntegerField(default=0)
    year = models.IntegerField(default=0)
    subject = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.name} ({self.neis})"