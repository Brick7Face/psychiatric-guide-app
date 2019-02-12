from django.contrib import admin
from application.models import Medication, Patient, Prescriber, Treatment, Step

admin.site.register(Step)
admin.site.register(Medication)
admin.site.register(Patient)
admin.site.register(Prescriber)
admin.site.register(Treatment)

