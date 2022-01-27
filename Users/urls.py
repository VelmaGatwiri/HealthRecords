from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='UsersHomepage'),
    path('hospital_register/', views.HospitalRegistration.as_view(), name='User-HospitalRegistration'),
    path('hospital/', views.hospital, name='HospitalModule'),

    path('patient/<str:pk>/', views.patient, name='PatientModule'),
    path('userDetails/<str:pk>/', views.user_details, name='UserDetailsModule'),
    path('patient_register/', views.PatientRegistration.as_view(), name='User-PatientRegistration'),

    path('admin/<str:pk>/', views.admin, name='AdminModule'),

    path('doctor/<str:pk>/', views.doctor, name='DoctorModule'),
    path('doctorDetails/<str:pk>/', views.doctor_details, name='DoctorDetailsModule'),
    path('doctor_register/', views.DoctorRegistration.as_view(), name='User-DoctorRegistration'),

    path('staff_Login/', views.login_view, name='Staff-Login'),

    path('records_pdf', views.records_pdf, name='records_Pdf'),
]
