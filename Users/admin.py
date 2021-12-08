from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin
from .models import Patient, Doctor, Administrator, Profile

admin.site.register(CustomUser, UserAdmin)
admin.site.register(Administrator)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Profile)

