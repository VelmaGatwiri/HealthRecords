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
