from datetime import datetime
from django.db.models.fields import DateField, DateTimeField
from users.models import Customer, Mechanic
from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields.related import ManyToManyField, OneToOneField
from django.utils.translation import gettext_lazy as _

# Create your models here.

class Service(models.Model):
    name = models.CharField(max_length=100, blank=False)
    cost = models.FloatField()

class Appointment(models.Model):
    class Status(models.TextChoices):
        BOOKED = 'BO', _('Booked')
        IN_SERVICE = 'IS', _('In Service')
        FIXED = 'FX', _('Fixed')
        COLLECTED = 'CL', _('Collected')
        UNREPAIRABLE = 'UR', _('Unrepairable')


    service_type = ManyToManyField('Service', blank=True, related_name='service_type')
    customer = ManyToManyField(Customer, blank=True, related_name='appointment_customer')
    mechanic = ManyToManyField(Mechanic, blank=True, related_name='appointment_mechanic')
    status = models.CharField(
        max_length=2,
        choices=Status.choices,
        default=Status.BOOKED)
    comments = models.CharField(max_length=150, blank=True)
    created_at = models.DateField(default=datetime.now)
    scheduled_at = models.CharField(max_length=15, blank=True)
    total_cost = models.FloatField()
    