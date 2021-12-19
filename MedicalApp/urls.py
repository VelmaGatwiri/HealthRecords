from django.urls import path
from . import views

urlpatterns = [
    path('patientModule/', views.patient, name='PatientRecordsModule'),
    path('recordModule/', views.records, name='RecordsModule'),
    path('appointmentModule/', views.appointment, name='AppointmentsModule'),
    path('prescriptionModule/', views.prescription, name='PrescriptionModule'),
    path('addRecord/', views.create_record, name='AddRecordModule'),
    path('addAppointment/', views.create_appointment, name='AddAppointmentModule'),
    path('addPrescription/', views.create_prescription, name='AddPrescriptionModule'),
]
