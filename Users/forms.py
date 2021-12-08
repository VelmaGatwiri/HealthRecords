from .models import CustomUser, Patient, Doctor, Profile
from MedicalApp.models import Hospital
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from django import forms
from django.forms import ModelForm


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )


class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "class": "form-control"
            }
        )
    )
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2', 'is_hospital', 'is_patient',
                  'is_doctor', 'is_administrator')


class PatientRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=250, required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    Phone_Number = forms.CharField(required=True)
    Physical_Address = forms.CharField()
    Date_Of_Birth = forms.DateField(required=True)
    Age = forms.CharField(required=True)
    UserSex = [('Male', 'M'),
               ('Female', 'F'),
               ('NotApplicable', 'N/A'), ]
    Sex = forms.ChoiceField(choices=UserSex, required=True)
    bloodGrp = [('A_positive', 'A+'),
               ('A_negative', 'A-'),
               ('B_positive', 'B+'),
               ('B_negative', 'B-'),
               ('O_positive', 'O+'),
               ('O_negative', 'O-'),
               ('AB_positive', 'AB+'),
               ('AB_negative', 'AB-'),
            ]
    Blood_Group = forms.ChoiceField(required=True, choices=bloodGrp)
    Allergies = forms.CharField(required=True)
    Next_Of_Kin = forms.CharField(required=True)

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.Phone_Number = self.cleaned_data.get('Phone Number')
        user.Physical_Address = self.cleaned_data.get('Physical_Address')
        user.Date_Of_Birth = self.cleaned_data.get('Date_Of_Birth')
        user.Age = self.cleaned_data.get('Age')
        user.Sex = self.cleaned_data.get('Sex')
        user.is_patient = True
        user.save()
        patient = Patient.objects.create(user=user)
        patient.Blood_Group = self.cleaned_data.get('Blood Group')
        patient.Allergies = self.cleaned_data.get('Allergies')
        patient.Next_Of_Kin = self.cleaned_data.get('Next_Of_Kin')
        patient.save()
        return user


class DoctorRegistrationForm(UserCreationForm):
    first_name = forms.CharField(max_length=250, required=True)
    last_name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    Phone_Number = forms.CharField(required=True)
    Physical_Address = forms.CharField(required=True)
    Date_Of_Birth = forms.DateField(required=True)
    Age = forms.CharField(required=True)
    UserSex = [('Male', 'M'),
               ('Female', 'F'),
               ('NotApplicable', 'N/A'), ]
    Sex = forms.ChoiceField(choices=UserSex, required=True)
    docSpecialty = [('Card', 'Cardiologist'),
                    ('Dent', 'Dentist'),
                    ('Derm', 'Dermatology'),
                    ('Neuro', 'Neurologist'),
                    ('Path', 'Pathology'),
                    ('Ped', 'Pediatrician'),
                    ('Phy', 'Physician'),
                    ('Ob_GYN', 'Obstetrician and Gynecologist'),
                    ('Onc', 'Oncologist'),]
    Specialty = forms.ChoiceField(required=True, choices=docSpecialty)

    class Meta(UserCreationForm.Meta):
        model = CustomUser

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.email = self.cleaned_data.get('email')
        user.Phone_Number = self.cleaned_data.get('Phone Number')
        user.Physical_Address = self.cleaned_data.get('Physical_Address')
        user.Date_Of_Birth = self.cleaned_data.get('Date_Of_Birth')
        user.Age = self.cleaned_data.get('Age')
        user.Sex = self.cleaned_data.get('Sex')
        user.is_doctor = True
        user.save()
        doctor = Doctor.objects.create(user=user)
        doctor.specialty = self.cleaned_data.get('Specialty')
        doctor.save()
        return user


class HospitalRegistrationForm(ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'Phone_Number', 'email', 'Physical_Address', 'Sex']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']