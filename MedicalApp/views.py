from .forms import *
from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from Codes.forms import CodeForm
from Users.models import CustomUser
from .utils import *


def records(request):
    records = Record.objects.all()

    return render(request, 'MedicalApp/RecordModule.html', {'records': records})


def prescription(request):
    presc = Prescription.objects.all()

    return render(request, 'MedicalApp/PrescriptionModule.html', {'presc': presc})


def appointment(request):
    appoint = Appointment.objects.all()

    return render(request, 'MedicalApp/AppointmentModule.html', {'appoint': appoint})


def create_record(request):
    form = RecordForm()
    if request.method == 'POST':
        form = RecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('RecordsModule')
    context = {'form': form}

    return render(request, 'MedicalApp/addRecord.html', context)


def create_appointment(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AppointmentsModule')
    context = {'form': form}

    return render(request, 'MedicalApp/addAppointment.html', context)


def create_prescription(request):
    form = PrescriptionForm()
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PrescriptionModule')
    context = {'form': form}

    return render(request, 'MedicalApp/addPrescription.html', context)


def auth_view(request):
    form = AuthenticationForm()
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['pk'] = user.pk
            return redirect('verify_view')
    return render(request, 'auth.html', {'form': form})


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