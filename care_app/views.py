# from msilib.schema import ListView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .decorators import admin_required, manager_required, user_required
from .forms import PatientForm, UserRegisterForm
from .models import *
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


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
    template_name = 'care_app/patient_detail.html'
    context_object_name = 'patient'


class PatientCreateView(CreateView):
    model = Patient
    form_class = PatientForm
    template_name = 'care_app/patient_form.html'
    success_url = '/'

    def form_valid(self, form):
        return super().form_valid(form)


class PatientUpdateView(UpdateView):
    model = Patient
    fields = ['name', 'email', 'phone', 'dob']
    template_name = 'care_app/update_patient.html'
    success_url = '/patient/{id}/'


class PatientDeleteView(DeleteView):
    model = Patient
    success_url = reverse_lazy('index')
    template_name = 'care_app/patient_confirm_delete.html'

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        return redirect(self.get_success_url())

def medication_list(request, patient_id):
    patient = Patient.objects.get(pk=patient_id)
    medications = Medication.objects.filter(patient=patient)
    return render(request, 'care_app/medication_list.html', {'patient': patient, 'medications': medications})

# Role based access control
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            if user.role == 'admin':
                user.user_permissions.set(Permission.objects.filter(codename__in=['add_patient', 'change_patient', 'delete_patient']))
            elif user.role == 'manager':
                user.user_permissions.set(Permission.objects.filter(codename__in=['change_patient']))
            else:
                # User role, no special permissions
                pass
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'care_app/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            # invalid login
            pass
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('index')

@login_required
def profile(request):
    user = request.user
    return render(request, 'care_app/profile.html' , {'user': user})

# User Authentication
@admin_required
def admin_view(request):
    return HttpResponse("Admin View")

@manager_required
def manager_view(request):
    return HttpResponse("Manager View")

@user_required
def user_view(request):
    return HttpResponse("User View")

@login_required
@admin_required
def admin_dashboard(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
@manager_required
def manager_dashboard(request):
    return render(request, 'profile.html', {'user': request.user})

@login_required
@user_required
def user_dashboard(request):
    return render(request, 'profile.html', {'user': request.user})




