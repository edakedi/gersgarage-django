from django.db import models

# Create your models here.

class Car(models.Model):
    category = models.CharField(max_length=50, blank=True)
    engine_type = models.CharField(max_length=50, blank=True)
    make = models.CharField(max_length=50, blank=True)
    licence_detail = models.CharField(max_length=100, blank=True)
