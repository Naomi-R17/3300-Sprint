# from msilib.schema import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from care_app.models import Patient
from django.urls import reverse_lazy
from .forms import PatientForm


# Create your views here.
def index(request):
    return render(request, 'care_app/index.html')


class PatientListView(ListView):
    model = Patient
    template_name = 'care_app/home.html'
    context_object_name = 'patients'

    def get_queryset(self):
        return Patient.objects.filter(is_active=True)


class PatientDetailView(DetailView):
    model = Patient
    template_name = 'care_app/patient_detail.html'  # Create this template for displaying patient details
    context_object_name = 'patient'


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'care_app/patient_form.html'
    success_url = '/'

    def form_valid(self, form):
        # Additional logic can be added here if needed
        return super().form_valid(form)


class PatientUpdateView(UpdateView):
    model = Patient
    fields = ['name', 'email', 'phone', 'dob']
    template_name = 'care_app/update_patient.html'
    success_url = '/patient/{id}/'


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')  # Redirect to the home page after deletion
    template_name = 'care_app/patient_confirm_delete.html'  # The template for the confirmation page

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())
