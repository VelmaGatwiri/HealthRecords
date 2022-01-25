from .forms import *
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from Codes.forms import CodeForm
from .utils import *
from django.views.generic import ListView, DetailView
from .models import *


class RecordsListView(ListView):
    model = Record
    template_name = 'MedicalApp/RecordModule.html'
    context_object_name = 'records'
    ordering = ['-Record_Date']


class RecordsDetailView(DetailView):
    model = Record


class AppointmentListView(ListView):
    model = Appointment
    template_name = 'MedicalApp/AppointmentModule.html'
    context_object_name = 'appoint'


class AppointmentDetailView(DetailView):
    model = Appointment


class PrescriptionListView(ListView):
    model = Prescription
    template_name = 'MedicalApp/PrescriptionModule.html'
    context_object_name = 'presc'


class PrescriptionDetailView(DetailView):
    model = Prescription


def create_record(request):
    form = RecordForm()
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AddPrescriptionModule')
    context = {'form': form}

    return render(request, 'MedicalApp/Record_form.html', context)


def update_record(request, pk):
    record = Record.objects.get(id=pk)
    form = RecordForm(instance=record)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('Records-Details')

    context = {'form': form}
    return render(request, 'MedicalApp/Record_form.html', context)


def delete_record(request, pk):
    record = Record.objects.get(id=pk)
    if request.method == "POST":
        record.delete()
        return redirect('Records-Details')
    context = {
        'item': record
    }
    return render(request, 'MedicalApp/delete_Record.html', context)


def create_appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('RecordsModule')
    context = {'form': form}

    return render(request, 'MedicalApp/Appointment_form.html', context)


def update_appointment(request, pk):
    app = Appointment.objects.get(id=pk)
    form = AppointmentForm(instance=app)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=app)
        if form.is_valid():
            form.save()
            return redirect('AppointmentsModule')

    context = {'form': form}
    return render(request, 'MedicalApp/Appointment_form.html', context)


def delete_appointment(request, pk):
    app = Appointment.objects.get(id=pk)
    context = {
        'item': app
    }
    return render(request, 'MedicalApp/delete_Appointment.html', context)


def create_prescription(request):
    form = PrescriptionForm()
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AddAppointmentModule')
    context = {'form': form}

    return render(request, 'MedicalApp/Prescription_form.html', context)


def update_prescription(request, pk):
    pre = Prescription.objects.get(id=pk)
    form = PrescriptionForm(instance=pre)
    if request.method == 'POST':
        form = RecordForm(request.POST, instance=pre)
        if form.is_valid():
            form.save()
            return redirect('PrescriptionModule')

    context = {'form': form}
    return render(request, 'MedicalApp/Appointment_form.html', context)


def delete_prescription(request, pk):
    pre = Prescription.objects.get(id=pk)
    context = {
        'item': pre
    }
    return render(request, 'MedicalApp/delete_Appointment.html', context)


def auth_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('verify_view')
    return render(request, 'Users/login.html', {'form': form})


def verify_view(request):
    form = CodeForm(request.POST or None)
    pk = request.session.get('pk')
    user = CustomUser.objects.get(pk=pk)
    if pk:
        user = CustomUser.objects.get(pk=pk)
        code = user.code
        code_user = f"{user.username}: {user.code}"
        if not request.POST:
            print(code_user)
            send_sms(code_user, user.Phone_Number)
        if form.is_valid():
            num = form.cleaned_data.get('number')

            if str(code) == num:
                code.save()
                login(request, user)
                return redirect('RecordsModule')
            else:
                return redirect('login')
    return render(request, 'verify.html', {'form': form})
