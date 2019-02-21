# Script to populate MySQL database with information from Prescribers Guide 2012.
# Currently only populates with treatments, corresponding steps, and medications
# Heavily consulted https://blog.robphoenix.com/python/notes-on-django-population-script/ for correct formatting, functionality of this script

import os

def populate():
   print('Populating database...\n')
   
   step1 = add_step('Step 1','fake description')
   add_treatment('Depression', step1)
   add_medication('Medication 1', 'fakes', 25, 50, 'wut', 'nothing', 'all the things')

   print('\n' + ('=' * 80) + '\n')

# add a step to database, with name and descriptions as strings
def add_step(name, description):
   s, created = Step.objects.get_or_create(name=name, description=description)

   print('- Step: {0}, Created: {1}'.format(str(s), str(created)))
   return s

# add treatment with name as string and step as reference to a step created previously
def add_treatment(name, *step):
   t, created = Treatment.objects.get_or_create(name=name)
   t.steps.add(*step)

   print('- Treatment: {0}, Created: {1}'.format(str(t), str(created)))
   return t

# add medication with name, category, titration, comments, and side effects as strings, others as floats
def add_medication(name, category, dose_i, dose_m, titration, comm, se):
   m, created = Medication.objects.get_or_create(name=name, category=category, initial_dose=dose_i, maximum_dose=dose_m, titration=titration, comments=comm, side_effects=se)
   
   print('- Medication: {0}, Created: {1}'.format(str(m), str(created)))
   return m

# run main from here
if __name__ == '__main__':
   print('\n' + ('=' * 80) + '\n')
   import django
   os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'psychiatric_guide_app.settings')

   django.setup()
   from application.models import Step, Medication, Treatment
   from django.contrib.auth.models import User
   from django.db import IntegrityError
   populate()
