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


# Medication list
class Medication(models.Model):
    MEDICATION_OPTIONS = (
        ('Acetaminophen', 'Acetaminophen'),
        ('Adderall', 'Adderall'),
        ('Amitriptyline', 'Amitriptyline'),
        ('Amlodipine', 'Amlodipine'),
        ('Amoxicillin', 'Amoxicillin'),
        ('Ativan', 'Ativan'),
        ('Atorvastatin', 'Atorvastatin'),
        ('Azithromycin', 'Azithromycin'),
        ('Benzonatate', 'Benzonatate'),
        ('Brilinta', 'Brilinta'),
        ('Bunavail', 'Bunavail'),
        ('Buprenophine', 'Buprenophine'),
        ('Cephalexin', 'Cephalexin'),
        ('Ciprofloxacin', 'Ciprofloxacin'),
        ('Citalopram', 'Citalopram'),
        ('Clindamycin', 'Clindamycin'),
        ('Clonazepam', 'Clonazepam'),
        ('Cyclobenzaprine', 'Cyclobenzaprine'),
        ('Cymbalta', 'Cymbalta'),
        ('Doxycycline', 'Doxycycline'),
        ('Dupixent', 'Dupixent'),
        ('Entresto', 'Entresto'),
        ('Entyvio', 'Entyvio'),
        ('Farxiga', 'Farxiga'),
        ('Fentaynl', 'Fentanyl'),
        ('Gabapentin', 'Gabapentin'),
        ('Gilenya', 'Gilenya'),
        ('Humira', 'Humira'),
        ('Hydrochlorothiazide', 'Hydrochlorothiazide'),
        ('Ibuprofen', 'Ibuprofen'),
        ('Imbruvica', 'Imbruvica'),
        ('Januvia', 'Januvia'),
        ('Kevzara', 'Kevzara'),
        ('Leqvio', 'Leqvio'),
        ('Lexapro', 'Lexapro'),
        ('Lisinopril', 'Lisinopril'),
        ('Lyrica', 'Lyrica'),
        ('Melatonin', 'Melatonin'),
        ('Meloxicam', 'Meloxicam'),
        ('Metformin', 'Metformin'),
        ('Methadone', 'Methadone'),
        ('Metoprolol', 'Metoprolol'),
        ('Naloxone', 'Naloxone'),
        ('Nurtec', 'Nurtec'),
        ('Omeprazole', 'Omeprazole'),
        ('Ozempic', 'Ozempic'),
        ('Pantoprazole', 'Pantoprazole'),
        ('Prednisone', 'Prednisone'),
        ('Tramadol', 'Tramadol'),
        ('Trazodone', 'Trazodone'),
        ('Viagra', 'Viagra'),
        ('Wellbutrin', 'Wellbutrin'),
        ('Xanax', 'Xanax')
    )
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    name = models.CharField("Medication Name", max_length=200, choices=MEDICATION_OPTIONS, blank=False)
    dosage = models.IntegerField("Dosage", blank=False)
    takenDaily = models.BooleanField("Taken Daily?", default=False)
    startDate = models.DateField("Starting Date", blank=False, null=False)
    endDate = models.DateField("Ending Date", blank=False, null=False)

    class Meta:
        verbose_name = "Medication"
        verbose_name_plural = "Medications"

    def __str__(self):
        return f"{self.patient.name}'s {self.name}"


