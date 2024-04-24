from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from care_app.views import PatientListView, PatientDetailView, PatientCreateView, PatientUpdateView, PatientDeleteView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.PatientListView.as_view(), name='index'),

    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # new paths
    path('patient/<int:pk>/', PatientDetailView.as_view(), name='patient-detail'),
    path('patient/create/', PatientCreateView.as_view(), name='patient-create'),
    path('patient/<int:pk>/update/', PatientUpdateView.as_view(), name='patient-update'),
    path('patient/<int:pk>/delete/', views.PatientDeleteView.as_view(), name='patient-delete'),

    # Medication List
    path('patient/<int:patient_id>/medications/', views.medication_list, name='medication-list'),

    # Register
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)