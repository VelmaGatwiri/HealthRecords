from django.db import models
from Users.models import CustomUser, Administrator, Patient, Doctor
from django.utils import timezone


class Hospital(models.Model):
    Hospital_Image = models.ImageField(default='default.png', upload_to='hospital_pics')
    Hospital_Name = models.CharField(max_length=100, blank=False)
    Hospital_Description = models.TextField()
    Registration_Date = models.DateTimeField(default=timezone.now)
    Admin_ID = models.ForeignKey(Administrator, on_delete=models.RESTRICT)

    def __str__(self):
        return self.Hospital_Name


class Record(models.Model):
    Patient_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor_ID = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    Hospital_ID = models.ForeignKey(Hospital, on_delete=models.RESTRICT)
    New_Diagnosis = models.TextField()
    Record_Date = models.DateField(default=timezone.now)

    def __str__(self):
        return str(self.Patient_ID)


class Appointment(models.Model):
    Patient_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor_ID = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    Hospital_ID = models.ForeignKey(Hospital, on_delete=models.RESTRICT)
    Record_ID = models.ForeignKey(Record, on_delete=models.RESTRICT)
    Appointment_Details = models.TextField()
    Appointment_Schedule = models.DateTimeField()
    Pending = 'Pending'
    Cancelled = 'Cancelled'
    Successful = 'Successful'
    Postponed = 'Postponed'
    AppointmentStatus = [(Pending, 'Pending'), (Cancelled, 'Cancelled'), (Successful, 'Successful'),
                         (Postponed, 'Postponed')
                         ]
    Appointment_Status = models.CharField(max_length=20, choices=AppointmentStatus, null=True, blank=True,
                                          default=Pending)

    def __str__(self):
        return str(self.Patient_ID)


class Prescription(models.Model):
    Patient_ID = models.ForeignKey(Patient, on_delete=models.CASCADE)
    Doctor_ID = models.ForeignKey(Doctor, on_delete=models.RESTRICT)
    Hospital_ID = models.ForeignKey(Hospital, on_delete=models.RESTRICT)
    Record_ID = models.ForeignKey(Record, on_delete=models.RESTRICT)
    Prescription_Details = models.TextField()

    def __str__(self):
        return str(self.Patient_ID)
