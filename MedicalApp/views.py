from django.shortcuts import render, redirect
from .forms import *


def patient(request):
    return render(request, 'MedicalApp/patientModule.html')


def records(request):
    records = Record.objects.all()

    return render(request, 'MedicalApp/RecordModule.html', {'records': records})


def prescription(request):
    presc = Prescription.objects.all()

    return render(request, 'MedicalApp/PrescriptionModule.html', {'presc': presc})


def appointment(request):
    appoint = Record.objects.all()

    return render(request, 'MedicalApp/AppointmentModule.html', {'appoint': appoint})


def createRecord(request):
    form = RecordForm()
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('RecordsModule')
    context = {'form': form}

    return render(request, 'MedicalApp/addRecord.html', context)
