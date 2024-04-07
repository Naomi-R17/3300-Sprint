from django.db import models
from django.urls import reverse


# Create your models here.
class Patient(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    phone = models.CharField("Phone Number", max_length=200, blank=False)
    dob = models.CharField("Date of Birth", max_length=200, blank=False)
    is_active = models.BooleanField(default=False)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('patient-detail', args=[str(self.id)])


