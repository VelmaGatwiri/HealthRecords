from django.db import models
from Users.models import CustomUser, Administrator, Patient, Doctor


class Hospital(models.Model):
    Hospital_Name = models.CharField(max_length=100, blank=False)
    Registration_Date = models.DateTimeField(auto_now_add=True)
    Admin_ID = models.ForeignKey(Administrator, on_delete=models.RESTRICT)

    def __str__(self):
        return self.Hospital_Name
