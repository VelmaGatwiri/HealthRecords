from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import Patient, Doctor, Administrator, Profile
from .forms import *

UserAdmin.fieldsets += ('Custom User Information', {'fields': ('Phone_Number', 'Physical_Address',
                                                               'Date_Of_Birth', 'Age', 'Sex', 'is_hospital',
                                                               'is_patient', 'is_doctor', 'is_administrator')}),

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Administrator)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Profile)

