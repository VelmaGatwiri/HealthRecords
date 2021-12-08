from django.urls import path
from . import views


urlpatterns = [
    path('', views.login_view, name='login'),
    path('patient_register/', views.PatientRegistration.as_view(), name='User-PatientRegistration'),
    path('doctor_register/', views.DoctorRegistration.as_view(), name='User-DoctorRegistration'),
    path('hospital_register/', views.HospitalRegistration.as_view(), name='User-HospitalRegistration'),
    path('patient/', views.patient, name='PatientModule'),
    path('admin/', views.admin, name='AdminModule'),
    path('doctor/', views.doctor, name='DoctorModule'),
    path('hospital/', views.hospital, name='HospitalModule'),
]
