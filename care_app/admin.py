from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Patient, Medication

admin.site.register(Patient)
admin.site.register(Medication)