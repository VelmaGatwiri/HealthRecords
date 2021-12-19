from django.forms import ModelForm
from .models import *
from django import forms


class RecordForm(ModelForm):
    class Meta:
        model = Record
        fields = ('Patient_ID', 'Doctor_ID', 'Hospital_ID', 'New_Diagnosis')

        widgets = {
            'Patient_ID': forms.Select(attrs={'class': 'form-control'}),
            'Doctor_ID': forms.Select(attrs={'class': 'form-control'}),
            'Hospital_ID': forms.Select(attrs={'class': 'form-control'}),
            'New_Diagnosis': forms.Textarea(attrs={'class': 'form-control'}),
        }


class AppointmentForm(ModelForm):
    class Meta:
        model = Appointment
        fields = ('Patient_ID', 'Doctor_ID', 'Hospital_ID', 'Record_ID', 'Appointment_Details',
                  'Appointment_Schedule')

        widgets = {
            'Patient_ID': forms.Select(attrs={'class': 'form-control'}),
            'Doctor_ID': forms.Select(attrs={'class': 'form-control'}),
            'Hospital_ID': forms.Select(attrs={'class': 'form-control'}),
            'Record_ID': forms.Select(attrs={'class': 'form-control'}),
            'Appointment_Details': forms.Textarea(attrs={'class': 'form-control'}),
            'Appointment_Schedule': forms.DateTimeInput(attrs={'class': 'form-control datetimepicker-input',
                                                               'data-target': '#id_Appointment_Schedule'}),
        }


class PrescriptionForm(ModelForm):
    class Meta:
        model = Prescription
        fields = ('Patient_ID', 'Doctor_ID', 'Hospital_ID', 'Record_ID', 'Prescription_Details')

        widgets = {
            'Patient_ID': forms.Select(attrs={'class': 'form-control'}),
            'Doctor_ID': forms.Select(attrs={'class': 'form-control'}),
            'Hospital_ID': forms.Select(attrs={'class': 'form-control'}),
            'Record_ID': forms.Select(attrs={'class': 'form-control'}),
            'Prescription_Details': forms.Textarea(attrs={'class': 'form-control'}),
        }
