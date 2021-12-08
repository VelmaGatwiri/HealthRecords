from django.urls import path
from . import views


urlpatterns = [
    path('patientModule/', views.patient, name='PatientRecordsModule'),
]