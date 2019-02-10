from django.contrib import admin
from application.models import Step, Medication, Patient, Prescriber

admin.site.register(Step)
admin.site.register(Medication)
admin.site.register(Patient)
admin.site.register(Prescriber)

