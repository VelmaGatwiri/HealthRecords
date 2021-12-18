from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import *
from django.shortcuts import render, redirect
from MedicalApp.models import *
from django.views.generic import CreateView
from .decorators import *


def home(request):
    return render(request, 'Users/Homepage.html')


@login_required
@allowed_users(allowed_roles=['Patient', 'Doctor'])
def patient(request):
    context = {
        'record': Record.objects.all()
    }
    return render(request, 'Users/PatientModule.html', context)


@login_required
@allowed_users(allowed_roles=['Admin'])
def admin(request):
    return render(request, 'Users/AdminModule.html')


@login_required
@allowed_users(allowed_roles=['Doctor'])
def doctor(request):
    return render(request, 'Users/DoctorModule.html')


@login_required
# @allowed_users(allowed_roles=['Hospital'])
def hospital(request):
    return render(request, 'Users/HospitalModule.html')


@unauthenticated_user
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_patient:
            login(request, user)
            return redirect('PatientModule')
        if user is not None and user.is_doctor:
            login(request, user)
            return redirect('DoctorModule')
        if user is not None and user.is_admin:
            login(request, user)
            return redirect('AdminModule')
        if user is not None and user.is_hospital:
            login(request, user)
            return redirect('HospitalModule')
        else:
            messages.info(request, 'Username ot Password is incorrect')

    context = {}
    return render(request, 'Users/login.html', context)


class PatientRegistration(CreateView):
    model = CustomUser
    form_class = PatientRegistrationForm
    template_name = 'Users/PatientRegistration.html'

    def validation(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class DoctorRegistration(CreateView):
    model = CustomUser
    form_class = DoctorRegistrationForm
    template_name = 'Users/DoctorRegistration.html'

    def validation(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('login')


class HospitalRegistration(CreateView):
    model = CustomUser
    form_class = HospitalRegistrationForm
    template_name = 'Users/HospitalRegistration.html'


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'Users/profile.html', context)
