import django_filters
from django_filters import DateFilter, CharFilter
from .models import *


class RecordFilter(django_filters.FilterSet):
    #    start_date = DateFilter(field_name="Record_Date", lookup_expr='gte')
    #    end_date = DateFilter(field_name="Record_Date", lookup_expr='lte')
    class Meta:
        model = Record
        fields = ('Patient_ID', 'Hospital_ID')


class RecordPatientFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name="Record_Date", lookup_expr='gte')
    end_date = DateFilter(field_name="Record_Date", lookup_expr='lte')

    class Meta:
        model = Record
        fields = ('Hospital_ID', 'Record_Date')


class AppointmentFilter(django_filters.FilterSet):
    class Meta:
        model = Appointment
        fields = ('Patient_ID', 'Appointment_Schedule', 'Appointment_Status')


class PrescriptionFilter(django_filters.FilterSet):
    prescriptionDets = CharFilter(field_name='Prescription_Details', lookup_expr='icontains')

    class Meta:
        model = Prescription
        fields = '__all__'
        exclude = ['Doctor_ID', 'Hospital_ID', 'Record_ID', 'Prescription_Details']
