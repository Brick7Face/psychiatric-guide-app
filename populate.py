# Script to populate MySQL database with information from Prescribers Guide 2012.
# Currently only populates with treatments, corresponding steps, and medications
# Heavily consulted https://blog.robphoenix.com/python/notes-on-django-population-script/ for correct formatting, functionality of this script

import os

def populate():
   print('Populating database...\n')
   
   # steps that are part of the depression treatment algorithm
   dstep1 = add_step('Diagnosis of Depression','')
   dstep2 = add_step('', 'Initial therapy with citalopram or sertraline (unless compelling indication for alternate agent) Address side effects and encourage adherence in 1 week. Evaluate response in 3-4 weeks')
   dstep3 = add_step('Non Response', 'Ensure medication adherence\n\nOptimize dose OR switch (alternate SSRI or non-SSRI')
   dstep4 = add_step('Partial Response','Optimize dose OR augment')
   dstep5 = add_step('Full Response','Continue same treatment for at least 4-9 months')
   dstep6 = add_step('','Evaluate Response in 3-4 weeks')
   dstep7 = add_step('Non Response','Switch to a different antidepressant (SSRI or non-SSRI)')
   dstep8 = add_step('Partial Response','Optimize dose OR augment OR switch')

   # add steps to a list, passed to treatment algorithm
   dstepList = []
   dstepList.append(dstep1)
   dstepList.append(dstep2)
   dstepList.append(dstep3)
   dstepList.append(dstep4)
   dstepList.append(dstep5)
   dstepList.append(dstep6)
   dstepList.append(dstep7)
   dstepList.append(dstep8)

   # add depression treatment, linking to steps
   add_treatment('Depression', dstepList)

   # add medications - SSRI's
   add_medication('Citalopram (Celexa)', 'Selective Serotonin Reuptake Inhibitors', 10, 40, 'May increase by 10-20 mg increments at intervals of no less than 1 week', '- QT prolongation\n- Caution in heart disease, drug interactions', 'Orthostatic hypotension: rare\nConduction abnormalities: rare\nSedation: unlikely\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): rare\nGI distress, nausea: common\nRestlessness, jitters, tremors: uncommon\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: common\nSeizures: rare\nWeight gain: unlikely\nAgranulocytosis: rare')
   add_medication('Escitalopram (Lexapro)', 'Selective Serotonin Reuptake Inhibitors', 10, 20, 'May increase to 20 mg daily after 4 weeks', '- Enantimoer of citalopram\n- No generic; expensive', 'Orthostatic hypotension: rare\nConduction abnormalities: rare\nSedation: unlikely\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): rare\nGI distress, nausea: common\nRestlessness, jitters, tremors: uncommon\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: common\nSeizures: rare\nWeight gain: unlikely\nAgranulocytosis: rare')
   add_medication('Fluoxetine (Prozac)', 'Selective Serotonin Reuptake Inhibitors', 10, 80, 'May increase by 10-20 mg increments after several weeks', '- Long half life so fewer withdrawal symptoms\n- Activating, more drug interactions', 'Orthostatic hypotension: rare\nConduction abnormalities: rare\nSedation: unlikely\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): rare\nGI distress, nausea: common\nRestlessness, jitters, tremors: uncommon\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: common\nSeizures: rare\nWeight gain: unlikely\nAgranulocytosis: rare')
   add_medication('Paroxetine (Paxil)', 'Selective Serotonin Reuptake Inhibitors', 10, 50, 'May increase by 10mg increments at intervals of no less than 1 week', '- More sedation, weight gain, anticholinergic side effects, drug interactions, withdrawal effects\n- CR may cause less GI distress', 'Orthostatic hypotension: rare\nConduction abnormalities: rare\nSedation: unlikely\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): rare\nGI distress, nausea: common\nRestlessness, jitters, tremors: uncommon\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: common\nSeizures: rare\nWeight gain: unlikely\nAgranulocytosis: rare')
   add_medication('Sertraline (Zoloft)', 'Selective Serotonin Reuptake Inhibitors', 25, 200, 'May increase by 25-50 mg increments at intervals of no less than 1 week', '- Fewer drug interactions\n- More diarrhea\n- Used in geriatric population', 'Orthostatic hypotension: rare\nConduction abnormalities: rare\nSedation: unlikely\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): rare\nGI distress, nausea: common\nRestlessness, jitters, tremors: uncommon\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: common\nSeizures: rare\nWeight gain: unlikely\nAgranulocytosis: rare')

   print('\n' + ('=' * 80) + '\n')

# add a step to database, with name and descriptions as strings
def add_step(name, description):
   s, created = Step.objects.get_or_create(name=name, description=description)

   print('- Step: {0}, Created: {1}'.format(str(s), str(created)))
   return s

# add treatment with name as string and step as reference to a step created previously
def add_treatment(name, *stepList):
   t, created = Treatment.objects.get_or_create(name=name)
   for step in stepList:
      t.steps.add(step)

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
