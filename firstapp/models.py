from django.db import models


# Create your models here.
class Alex(models.Model):
    context = models.CharField(max_length=30)
    title = models.CharField(max_length=30)
    slug = models.CharField(max_length=30)
