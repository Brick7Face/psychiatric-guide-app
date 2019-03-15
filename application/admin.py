from django.contrib import admin
from application.models import Medication, Patient, Treatment, Step, Prescriber, Phq9

admin.site.register(Step)
admin.site.register(Medication)
admin.site.register(Patient)
admin.site.register(Prescriber)
admin.site.register(Treatment)
admin.site.register(Phq9)

class MyModelAdmin(admin.ModelAdmin):
    change_form_template = '/application/templates/admin/custom_change_template.html'

