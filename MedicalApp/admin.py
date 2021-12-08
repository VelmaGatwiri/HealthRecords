from django.contrib import admin
from .models import *

admin.site.register(Hospital)
admin.site.register(Appointment)
admin.site.register(Prescription)
admin.site.register(Record)

