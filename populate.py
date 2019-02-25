# Script to populate MySQL database with information from Prescribers Guide 2012.
# Currently only populates with treatments, corresponding steps, and medications
# Heavily consulted https://blog.robphoenix.com/python/notes-on-django-population-script/ for correct formatting, functionality of this script

import os
import datetime


def populate():
    print('Populating database...\n')

    step1 = add_step('Step 1', 'fake description')
    add_treatment('Depression', step1)
    m = add_medication('Medication 1', 'fakes', 25, 50, 'wut', 'nothing', 'all the things')
    add_patient('bp', 'plant', datetime.date.min, 'the ground', 'bp@email.com', '23456789', step1,
                datetime.datetime.min, [m], 'he is great')
    add_patient('k', 'dub', datetime.date.min, 'fun road', 'kdub@email.com', '234543789', step1,
                datetime.datetime.min, [m], 'she is the greatest')
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
    m, created = Medication.objects.get_or_create(name=name, category=category, initial_dose=dose_i,
                                                  maximum_dose=dose_m, titration=titration, comments=comm,
                                                  side_effects=se)

    print('- Medication: {0}, Created: {1}'.format(str(m), str(created)))
    return m


def add_patient(first_name, last_name, dob, address, email, phone,
                current_step, next_visit, medications, notes):
    p, created = Patient.objects.get_or_create(first_name=first_name,
                                               last_name=last_name,
                                               dob=dob,
                                               address=address,
                                               email=email,
                                               phone=phone,
                                               current_step=current_step,
                                               next_visit=next_visit,
                                               notes=notes)
    p.medications.set(medications)
    print('-Patient: {0}, Created: {1}'.format(str(p), str(created)))
    return p


# run main from here
if __name__ == '__main__':
    print('\n' + ('=' * 80) + '\n')
    import django

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'psychiatric_guide_app.settings')

    django.setup()
    from application.models import Step, Medication, Treatment, Patient
    from django.contrib.auth.models import User
    from django.db import IntegrityError

    populate()
