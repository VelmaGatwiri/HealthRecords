from django.db import models
from Users.models import CustomUser, Administrator, Patient, Doctor
from django.utils import timezone


class Hospital(models.Model):
    Hospital_Name = models.CharField(max_length=100, blank=False)
    Registration_Date = models.DateTimeField(default=timezone.now)
    Admin_ID = models.ForeignKey(Administrator, on_delete=models.RESTRICT)

    def __str__(self):
        return self.Hospital_Name


class Appointment(models.Model):
    Patient_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor_ID = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    Hospital_ID = models.ForeignKey(Hospital, on_delete=models.RESTRICT)
    Appointment_Details = models.TextField()
    Appointment_Schedule = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)


class Prescription(models.Model):
    Patient_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor_ID = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    Hospital_ID = models.ForeignKey(Hospital, on_delete=models.RESTRICT)
    Prescription_Details = models.TextField()

    def __str__(self):
        return str(self.id)


class Record(models.Model):
    Patient_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor_ID = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    Hospital_ID = models.ForeignKey(Hospital, on_delete=models.RESTRICT)
    Appointment_ID = models.ForeignKey(Appointment, on_delete=models.RESTRICT)
    Prescription_ID = models.ForeignKey(Prescription, on_delete=models.RESTRICT)
    New_Diagnosis = models.TextField()
    Record_Date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)
