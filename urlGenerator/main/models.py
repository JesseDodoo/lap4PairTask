from django.db import models

# Create your models here.
class short_url(models.Model):
    short_url = models.Charfield(max_length=20)
    long_url = models.URLField("URL", unique=True)
    

