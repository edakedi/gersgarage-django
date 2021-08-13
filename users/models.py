from django.db import models
from django.contrib.auth.models import User
from django.db.models.fields import CharField
from django.db.models.fields.related import OneToOneField
from django.urls import reverse
from django.utils import timezone
from django.conf import settings
from autoslug import AutoSlugField

from datetime import datetime

class Car(models.Model):
    category = models.CharField(max_length=50, blank=True)
    engine_type = models.CharField(max_length=50, blank=True)
    make = models.CharField(max_length=50, blank=True)
    licence_detail = models.CharField(max_length=100, blank=True)

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='user')
    phone_number = CharField(max_length=12, blank=True)
    car = OneToOneField(Car, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.username)
    
    def get_absolute_url(self):
        return "/{}".format(self.slug)

class Mechanic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    slug = AutoSlugField(populate_from='user')

    def __str__(self):
        return str(self.user.username)