from django.shortcuts import render
from .models import Record


def patient(request):
    rec = Record.objects.all().order_by('Record_Date')
    return render(request, 'MedicalApp/patientModule.html', {'rec': rec})
