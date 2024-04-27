from django import forms
from .models import Patient, CustomUser
from django.contrib.auth.forms import UserCreationForm


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ['name', 'email', 'phone', 'dob', 'is_active', 'profile_picture']

# Registration
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('user', 'User'),
    )
    role = forms.ChoiceField(choices=ROLE_CHOICES)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password1', 'password2', 'role']


