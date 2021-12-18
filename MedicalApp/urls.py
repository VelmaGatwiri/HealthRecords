from django.urls import path
from . import views


urlpatterns = [
    path('patientModule/', views.patient, name='PatientRecordsModule'),
    path('recordModule/', views.records, name='RecordsModule'),
    path('addRecord/', views.createRecord, name='AddRecordModule'),
]