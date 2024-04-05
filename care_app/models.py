from django.db import models


# Create your models here.
class Patient(models.Model):
    # starting off with very basic information, all required
    name = models.CharField(max_length=200, blank=False)
    email = models.CharField("Email", max_length=200, blank=False)
    phone = models.CharField("Phone Number", max_length=200, blank=False)
    dob = models.CharField("Date of Birth", max_length=200, blank=False)
