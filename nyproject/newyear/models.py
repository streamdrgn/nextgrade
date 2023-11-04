from django.db import models

class Survey(models.Model):
    name = models.CharField(max_length=255)
    neis = models.CharField(max_length=4)
    career = models.IntegerField()
    department = models.IntegerField()
    year = models.IntegerField()
    subject = models.IntegerField()

    def __str__(self):
        return f"{self.name} ({self.neis})"