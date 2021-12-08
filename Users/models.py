from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(null=False)
    Phone_Number = models.CharField(max_length=14, null=True)
    Physical_Address = models.TextField(null=True)
    Date_Of_Birth = models.DateField(auto_now=False, null=True)
    Age = models.CharField(max_length=3, null=True)
    Male = 'M'
    Female = 'F'
    NotApplicable = 'N/A'
    SEX_CHOICES = [(Male, 'M'), (Female, 'F'), (NotApplicable, 'N/A'), ]
    Sex = models.CharField(max_length=30, choices=SEX_CHOICES, null=True)
    is_patient = models.BooleanField('is_patient', default=True)
    is_doctor = models.BooleanField('is_doctor', default=False)
    is_administrator = models.BooleanField('is_administrator', default=False)
    is_hospital = models.BooleanField('is_hospital', default=False)

    def __str__(self):
        return self.username


class Patient(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    A_positive = 'A+'
    A_negative = 'A-'
    B_positive = 'B+'
    B_negative = 'B-'
    O_positive = 'O+'
    O_negative = 'O-'
    AB_positive = 'AB+'
    AB_negative = 'AB-'
    BLOOD_GROUP_CHOICES = [(A_positive, 'A+'), (A_negative, 'A-'), (B_positive, 'B+'),
                           (B_negative, 'B-'), (O_positive, 'O+'), (O_negative, 'O-'), (AB_positive, 'AB+'),
                           (AB_negative, 'AB-'),
                           ]
    Blood_Group = models.CharField(max_length=4, choices=BLOOD_GROUP_CHOICES, null=True, blank=True,
                                   default=AB_positive)
    Allergies = models.TextField(null=True, blank=True)
    Next_Of_Kin = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Patient Module'

    def __str__(self):
        return str(self.user)


class Doctor(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    Card = 'Cardiologist'
    Dent = 'Dentist'
    Derm = 'Dermatology'
    Neuro = 'Neurologist'
    Path = 'Pathology'
    Ped = 'Pediatrician'
    Phy = 'Physician'
    Ob_GYN = 'Obstetrician and Gynecologist'
    Onc = 'Oncologist'
    SPECIALTY = [(Card, 'Cardiologist'), (Dent, 'Dentist'), (Derm, 'Dermatology'),
                           (Neuro, 'Neurologist'), (Path, 'Pathology'), (Ped, 'Pediatrician'), (Phy, 'Physician'),
                           (Ob_GYN, 'Obstetrician and Gynecologist'), (Onc, 'Oncologist'), ]
    specialty = models.CharField(max_length=50, choices=SPECIALTY, null=True, blank=True, default=Phy)

    class Meta:
        verbose_name = 'Doctor Module'

    def __str__(self):
        return str(self.user)


class Administrator(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)

    class Meta:
        verbose_name = 'Administrator Module'

    def __str__(self):
        return str(self.user)


class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
