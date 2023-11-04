from django.db import models

class Information(models.Model):
  name = models.CharField(max_length=100)

def save(self, *args, **kwargs):
  super().save(*args, **kwargs)
  print(self.name)
