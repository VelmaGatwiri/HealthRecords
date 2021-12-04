from django.contrib.auth import login
from .forms import CustomUserCreationForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .decorators import allowed_users
from .forms import *
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import CreateView


def home(request):
    return render(request, 'Users/userDash.html')


def patient(request):
    return render(request, 'Users/PatientModule.html')


def admin(request):
    return render(request, 'Users/AdminModule.html')


def doctor(request):
    return render(request, 'Users/DoctorModule.html')


def hospital(request):
    return render(request, 'Users/HospitalModule.html')


class PatientRegistration(CreateView):
    model = CustomUser
    form_class = PatientRegistrationForm
    template_name = 'Users/PatientRegistration.html'

    def validation(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('PatientModule')


class DoctorRegistration(CreateView):
    model = CustomUser
    form_class = DoctorRegistrationForm
    template_name = 'Users/DoctorRegistration.html'

    def validation(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('DoctorModule')


class HospitalRegistration(CreateView):
    model = CustomUser
    form_class = HospitalRegistrationForm
    template_name = 'Users/HospitalRegistration.html'

    def validation(self, form):
        hospital = form.save()
        login(self.request, hospital)
        return redirect('HospitalModule')


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
