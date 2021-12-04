from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from Users import views as user_views


urlpatterns = [
    path('', auth_views.LoginView.as_view(template_name='Users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='Users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('patient_register/', views.PatientRegistration.as_view(), name='User-PatientRegistration'),
    path('doctor_register/', views.DoctorRegistration.as_view(), name='User-DoctorRegistration'),
    path('hospital_register/', views.HospitalRegistration.as_view(), name='User-HospitalRegistration'),
    path('home/', views.home, name='User-home'),
    path('patient/', views.home, name='PatientModule'),
    path('admin/', views.admin, name='AdminModule'),
    path('doctor/', views.doctor, name='DoctorModule'),
    path('hospital/', views.hospital, name='HospitalModule'),
]
