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
   add_medication('Fluoxetine (Prozac)', 'Selective Serotonin Reuptake Inhibitors', 10, 80, 'May increase by 10-20 mg increments after several weeks', '- Long half life so fewer withdrawal symptoms\n- Activating, more drug interactions\n- take in the morning, most potients respond to 20-40 mg daily', 'Orthostatic hypotension: rare\nConduction abnormalities: rare\nSedation: unlikely\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): rare\nGI distress, nausea: common\nRestlessness, jitters, tremors: uncommon\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: common\nSeizures: rare\nWeight gain: unlikely\nAgranulocytosis: rare')
   add_medication('Paroxetine (Paxil)', 'Selective Serotonin Reuptake Inhibitors', 10, 50, 'May increase by 10mg increments at intervals of no less than 1 week', '- More sedation, weight gain, anticholinergic side effects, drug interactions, withdrawal effects\n- CR may cause less GI distress\n- take at bedtime', 'Orthostatic hypotension: rare\nConduction abnormalities: rare\nSedation: unlikely\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): rare\nGI distress, nausea: common\nRestlessness, jitters, tremors: uncommon\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: common\nSeizures: rare\nWeight gain: unlikely\nAgranulocytosis: rare')
   add_medication('Sertraline (Zoloft)', 'Selective Serotonin Reuptake Inhibitors', 25, 200, 'May increase by 25-50 mg increments at intervals of no less than 1 week', '- Fewer drug interactions\n- More diarrhea\n- Used in geriatric population', 'Orthostatic hypotension: rare\nConduction abnormalities: rare\nSedation: unlikely\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): rare\nGI distress, nausea: common\nRestlessness, jitters, tremors: uncommon\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: common\nSeizures: rare\nWeight gain: unlikely\nAgranulocytosis: rare')
   
   # add medications - Bupropion
   add_medication('Bupropion (Wellbutrin)', 'Bupropion', 100, 450, 'IR: may increase after 4 days if tolerated (4 hours between doses, max single dose 150 mg)', '- Contraindicated in patients with bulimia, anorexia nervosa, and seizures\n- Low incidence of sexual disfunction, weight gain\n- Activating, insomnia; avoid bedtime dosing\n- May be helpful for ADHD and smoking cessation', 'Orthostatic hypotension: rare\nConduction abnormalities: unlikely\nSedation: rare\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): rare\nGI distress, nausea: uncommon\nRestlessness, jitters, tremors: common\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: rare\nSeizures: uncommon\nWeight gain: unlikely\nAgranulocytosis: rare')
   add_medication('Bupropion (Wellbutrin SR)', 'Bupropion', 150, 400, 'SR: may increase to 150 mg BID by day 4 if tolerated (8 hours between doses)', '- Contraindicated in patients with bulimia, anorexia nervosa, and seizures\n- Low incidence of sexual disfunction, weight gain\n- Activating, insomnia; avoid bedtime dosing\n- May be helpful for ADHD and smoking cessation', 'Orthostatic hypotension: rare\nConduction abnormalities: unlikely\nSedation: rare\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): rare\nGI distress, nausea: uncommon\nRestlessness, jitters, tremors: common\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: rare\nSeizures: uncommon\nWeight gain: unlikely\nAgranulocytosis: rare')
   add_medication('Bupropion (Wellbutrin XL)', 'Bupropion', 150, 450, 'XL: may increase to 300mg/day by day 4 if tolerated', '- Contraindicated in patients with bulimia, anorexia nervosa, and seizures\n- Low incidence of sexual disfunction, weight gain\n- Activating, insomnia; avoid bedtime dosing\n- May be helpful for ADHD and smoking cessation', 'Orthostatic hypotension: rare\nConduction abnormalities: unlikely\nSedation: rare\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): rare\nGI distress, nausea: uncommon\nRestlessness, jitters, tremors: common\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: rare\nSeizures: uncommon\nWeight gain: unlikely\nAgranulocytosis: rare')

   # add medications - SNRI's
   add_medication('Duloxetine (Cymbalta)', 'Serotonin-Norepinephrine Reuptake Inhibitors', 40, 120, 'Start at 30 mg daily for 1 week if tolerability is a concern, then increase dose', '- No generic, expensive\n- Contraindicated in patients with narrow angle glaucoma\n- may be given in divided doses, no additional benefit >60 mg/day', 'Orthostatic hypotension: unlikely\nConduction abnormalities: unlikely\nSedation: unlikely\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): unlikely\nGI distress, nausea: common\nRestlessness, jitters, tremors: uncommon\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: common\nSeizures: rare\nWeight gain: unlikely\nAgranulocytosis: rare')
   add_medication('Venlafaxine (Effexor)', 'Serotonin-Norepinephrine Reuptake Inhibitors', 37.5, 375, 'May increase by 75 mg increments at intervals of at least 4 days', '- take in divided doses', 'Orthostatic hypotension: unlikely\nConduction abnormalities: unlikely\nSedation: unlikely\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): unlikely\nGI distress, nausea: common\nRestlessness, jitters, tremors: uncommon\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: common\nSeizures: rare\nWeight gain: unlikely\nAgranulocytosis: rare')
   add_medication('Venlafaxine (Effexor XR)', 'Serotonin-Norepinephrine Reuptake Inhibitors', 37.5, 225, 'XR: 37.5 mg in AM then increase to 75 mg in AM after 1 week, 150 mg in AM after 2 weeks; if partial response after 4 weeks may increase to 225 mg in AM', '- Less GI irritation', 'Orthostatic hypotension: unlikely\nConduction abnormalities: unlikely\nSedation: unlikely\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): unlikely\nGI distress, nausea: common\nRestlessness, jitters, tremors: uncommon\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: common\nSeizures: rare\nWeight gain: unlikely\nAgranulocytosis: rare')
   add_medication('Desvenlafaxine (Pristiq)', 'Serotonin-Norepinephrine Reuptake Inhibitors', 50, 400, 'Titrate as tolerated', '- Metabolite of venlafaxine\n- No generic, expensive\n- no additional benefit >50 mg/day', 'Orthostatic hypotension: unlikely\nConduction abnormalities: unlikely\nSedation: unlikely\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): unlikely\nGI distress, nausea: common\nRestlessness, jitters, tremors: uncommon\nHeadache: uncommon\nInsomnia: uncommon\nSexual dysfunction: common\nSeizures: rare\nWeight gain: unlikely\nAgranulocytosis: rare')
   
   # add medication - Mirtazapine
   add_medication('Mirtazapine (Remeron)', 'Mirtazapine', 15, 45, 'May increase dose by 15 mg increments at intervals of 1 or 2 weeks', '- Less sexual dysfunction\n- Sedating; may be less sedating as dose is increased\n- May stimulate appetite, weight gain\n- take at bedtime', 'Orthostatic hypotension: uncommon\nConduction abnormalities: unlikely\nSedation: uncommon\nAnticholinergic (dry mouth/eyes, constipation, urinary retention, tachycardia): unlikely\nGI distress, nausea: unlikely\nRestlessness, jitters, tremors: rare\nHeadache: rare\nInsomnia: rare\nSexual dysfunction: rare\nSeizures: unlikely\nWeight gain: common\nAgranulocytosis: unlikely')
   
   # add medications - Antidepressant Augmenting Agents
   add_medication('Buspirone (BuSpar)', 'Antidepressant Augmenting Agents', 15, 60, '', '- Give in divided doses\n- increase by 15 mg/day each week until week 3, then 60 mg/day after week 5', 'Dizziness, nausea, headache, nervousness, diarrhea')
   add_medication('Bupropion (Wellbutrin SR)', 'Antidepressant Augmenting Agents', 200, 400, '', '- Give in divided doses\n- 200 mg/day for 2 weeks, 300 mg/day by week 4, 400 mg/day week 6', 'Restlessness, insomnia, nausia, headache, seizures, also refer to Bupropion side effects')
   add_medication('Liothyronine (Cytomel)', 'Antidepressant Augmenting Agents', 0.025, 0.050, '', '- Monitor BUN/Cr in elderly patients\n- Response usually within 3 weeks\n- take initial dose for 1 week then 0.050 mg/day', 'May aggravate cardiac conditions, symptoms of excessive dosage: anorexia, diaphoresis, heat intolerance, nausea/vomiting, tremor')
   add_medication('Lithium (Eskalith, Lithobid)', 'Antidepressant Augmenting Agents', 450, 900, '', '- Therapeutic level: may be lower for depression augmentation\n- Avoid in renal impairment\n- Also see bipolar medications\n- take at bedtime, descrease to 225 mg if not tolerated initially, 900 mg/day after 1 week', 'Gastrointestinal distress, polydipsia/polyuria, acne, weight gain, fine hand tremor')
   add_medication('Quetiapine (Seroquel, Seroquel XR)', 'Antidepressant Augmenting Agents', 50, 300, '', '- Monitor blood glucose, liver enzymes, lipids, weight, movement disorder side effects\n- take at bedtime for 2 days, then 150 mg for 2 days', 'Hypotension, somnolence ,sedation, headache, agitation, dizziness, endocrine and metabolic changes, dry mouth, weight gain, extrapyramidal symptoms')
   add_medication('Aripiprazole (Abilify)', 'Antidepressant Augmenting Agents', 2, 15, 'Increase by up to 5 mg/day at one week intervals', '- Monitor blood glucose, liver enzymes, lipids, weight, movement disorder side effects\n- Antipsychotic with least weight gain', 'Headache, agitation, insomnia, somnolence, extrapyramidal symptoms, nausea, dyspepsia')
   
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
