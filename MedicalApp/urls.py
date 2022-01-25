from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('recordModule/', RecordsListView.as_view(), name='RecordsModule'),
    path('record/<str:pk>/', RecordsDetailView.as_view(), name='Records-Details'),
    path('addRecord/', views.create_record, name='AddRecordModule'),
    path('updateRecord/<str:pk>', views.update_record, name='UpdateRecordModule'),
    path('deleteRecord/<str:pk>', views.delete_record, name='DeleteRecordModule'),

    path('appointmentModule/', AppointmentListView.as_view(), name='AppointmentsModule'),
    path('appointment/<str:pk>/', AppointmentDetailView.as_view(), name='Appointment-Details'),
    path('addAppointment/', views.create_appointment, name='AddAppointmentModule'),
    path('updateAppointment/<str:pk>', views.update_appointment, name='UpdateAppointmentModule'),
    path('deleteAppointment/<str:pk>', views.delete_appointment, name='DeleteAppointmentModule'),

    path('prescriptionModule/', PrescriptionListView.as_view(), name='PrescriptionModule'),
    path('prescription/<str:pk>/', PrescriptionDetailView.as_view(), name='Prescription-Details'),
    path('addPrescription/', views.create_prescription, name='AddPrescriptionModule'),
    path('updatePrescription/<str:pk>', views.update_prescription, name='UpdatePrescriptionModule'),
    path('deleteRecord/<str:pk>', views.delete_prescription, name='DeletePrescriptionModule'),
]
