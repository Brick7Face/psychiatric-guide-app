import datetime
import json
import os
import re

import praw
from django.db.models import Model
from django.forms import Form
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core import serializers
from django.template.defaulttags import register
from django.views.generic.edit import UpdateView
from django.forms import ModelForm
from django.db import models


from application.models import Prescriber, Step, Patient, Treatment, Medication
from application.models import Phq9 as phq9_db
from application.models import MDQ as mdq_db
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from application.questionnaire_evaluations import PHQ9
from application.questionnaire_evaluations import MDQ

from google.cloud import datastore
from github import Github


def login(request):
    return render(request, 'application/login.html', {'title': 'Login'})  # Renders login.html


def logout_user(request):
    logout(request)  # Built in django logout function
    return redirect('login-view')  # Logs user out and redirects to login page


# Create user code helped from Youtube series by Cory Schafer: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
@login_required  # If user is not logged in, they are redirected to the login page.
def create_user(request):  # Renders user creation
    if request.method == 'POST':
        new_user_form = CreateUser(request.POST) # Form for creating a new user
        if new_user_form.is_valid():  # Enters if form is valid
            new_user_form.save()  # Saves form to database
            username = new_user_form.cleaned_data.get('username')
            first_name = new_user_form.cleaned_data.get('first_name')
            last_name = new_user_form.cleaned_data.get('last_name')
            messages.success(request, 'Account created.')  # Message if user created succesfully
            return redirect('create-new-user')

    else:
        new_user_form = CreateUser()  # Resets form with error message if attempt not valid
    return render(request, 'application/new-user.html', {'new_user_form': new_user_form})


class CreateUser(UserCreationForm):  # Class for the user generation form
    username = forms.CharField()  # gets username
    first_name = forms.CharField()  # gets first name
    last_name = forms.CharField()  # Gets last name.
    is_super_user = forms.CheckboxInput()  # checkbox for superuser
    is_staff = forms.CheckboxInput()  # checkbox for staff member

    class Meta:
        model = User  # Form is of User Model.
        fields = ['username', 'first_name', 'last_name', 'is_staff', 'is_superuser',
                  'password1']  # Fields to be displayed of the form on the site.
        help_texts = {  # Text descriptions that show under the field on the form
            'is_staff': 'Check if account is for a staff member.',
            'is_superuser': 'Allows this user to create, modify, edit, and delete other users and their information.'
        }

@login_required
def edit_algorithm(request):
    if request.method == 'POST':
        action = request.POST['action']
        step_id = request.POST['step_id']
        if action == "goto":
            request.session['step_id'] = step_id
            return redirect('/admin/application/step/%s/change/' % step_id)
        elif action == "delete":
            try:
                step = Step.objects.get(id=step_id)
                step.delete()
            except:
                pass

    return render(request, 'application/edit-algorithm.html', {'title': 'Edit Algorithm', 'steps': Step.objects.all()})


@login_required
def edit_medications(request):
    if request.method == 'POST':
        action = request.POST['action']
        medication_id = request.POST['medication_id']
        if action == "goto":
            request.session['medication_id'] = medication_id
            return redirect('/admin/application/medication/%s/change/' % medication_id)
        elif action == "delete":
            try:
                medication = Medication.objects.get(id=medication_id)
                medication.delete()
            except:
                pass

    return render(request, 'application/edit-medications.html', {'title': 'Edit Medications', 'medications': Medication.objects.all()})

class CreateMedicationForm(forms.ModelForm):
    name = forms.CharField()
    category = forms.CharField()
    initial_dose = forms.FloatField()
    maximum_dose = forms.FloatField()
    titration = forms.TextInput()
    comments = forms.TextInput()
    side_effects = forms.TextInput()

    class Meta:
        model = Medication
        fields = ['name', 'category', 'initial_dose', 'maximum_dose', 'titration', 'comments', 'side_effects']

@login_required  # If user is not logged in, they are redirected to the login page.
def new_medication(request):
    if request.method == 'POST':
        new_med_form = CreateMedicationForm(request.POST)
        if new_med_form.is_valid():
            new_med_form.save()
            messages.success(request, 'Medication created.')
            return redirect('edit-medications')
    else:
        new_med_form = CreateMedicationForm()
    return render(request, 'application/new-medication.html', {'new_med_form': new_med_form})

@login_required  # If user is not logged in, they are redirected to the login page.
def backend_home(request):
    return render(request, 'application/backend-home.html', {'title': 'Home'})  # Renders login.html


@login_required  # If user is not logged in, they are redirected to the login page.
def patients(request):
    if request.method == 'POST':
        action = request.POST['action']
        patient_id = request.POST['patient_id']
        # navigate to patient home
        if action == "goto":
            request.session['patient_id'] = patient_id
            return redirect('patient-home')
        # delete patient from database
        elif action == "delete":
            try:
                patient = Patient.objects.get(id=patient_id)
                patient.delete()
            except:
                pass

    return render(request, 'application/patients.html', {'title': 'Patients', 'patients': Patient.objects.all()})


@register.filter
def get_item(dictionary, key):
    return dictionary.get(key)


@login_required
def patient_home(request):
    if request.method == 'GET':
        action = request.GET.get('action', None)
        if action in ['phq9', 'mdq']:
            # take either phq9 or mdq survey
            request.session['patient_id'] = request.GET['patient_id']
            request.session['survey_type'] = action
            return redirect('survey')

    patient_id = request.session["patient_id"]
    return render(request, 'application/patient-home.html',
                  {'title': 'Patient Home',
                   'patient': Patient.objects.get(id=patient_id),
                   'phq9s': phq9_db.objects.filter(patient_id=patient_id),
                   'mdqs': mdq_db.objects.filter(patient_id=patient_id)})  # Renders login.html


def documentation(request):
    return render(request, 'application/documentation.html', {'title': 'Documentation'})  # Renders login.html


@login_required  # If user is not logged in, they are redirected to the login page.
def survey(request):
    survey_type = request.session['survey_type']
    if request.method == 'POST':
        results = dict(request.POST)
        results.pop('csrfmiddlewaretoken', '')
        print(results)

        if survey_type == 'phq9':
            return process_phq9(request, results)
        elif survey_type == 'mdq':
            return process_mdq(request, results)
    else:
        if survey_type == 'phq9':
            return get_phq9(request)
        elif survey_type == 'mdq':
            return get_mdq(request)


@login_required
def survey_results(request):
    survey_type = request.session['survey_type']
    if request.method == 'POST':
        if survey_type == 'phq9':
            # add phq-9 results to the patient
            patient_id = request.session['patient_id']
            phq9 = phq9_db.objects.get(id=request.session['survey_id'])
            phq9.patient_id = patient_id
            phq9.save()
        elif survey_type == 'mdq':
            # add mdq results to the patient
            patient_id = request.session['patient_id']
            mdq = mdq_db.objects.get(id=request.session['survey_id'])
            mdq.patient_id = patient_id
            mdq.save()
        return redirect('patient-home')
    else:
        if survey_type == 'phq9':
            # display phq9 results
            dict = {'diagnosis': phq9_db.objects.last().diagnosis,
                    'change_treatment': phq9_db.objects.last().change_treatment,
                    'suicide_risk': phq9_db.objects.last().suicide_risk,
                    'severity_score': phq9_db.objects.last().severity_score}
            return render(request, 'application/phq9-results.html', dict)
        elif survey_type == 'mdq':
            # display mdq results
            dict = {}
            return render(request, 'application/mdq-results.html', dict)


def get_phq9(request):
    introduction = "Over the past 2 weeks, how often have you been bothered by any of the following problems?"
    choices1 = ["Not at all", "Several days", "More than half the days", "Nearly every day"]
    choices2 = ["Not difficult at all", "Somewhat difficult", "Very difficult", "Extremely difficult"]
    questions = [
        ["Little interest or pleasure in doing things?", choices1],
        ["Feeling down, depressed or hopeless?", choices1],
        ["Trouble falling or staying asleep, or sleeping too much?", choices1],
        ["Feeling tired or having little energy?", choices1],
        ["Poor appetite or overeating?", choices1],
        ["Feeling bad about yourself or that you are a failure or have let yourself or your family down?",
         choices1],
        ["Trouble concentrating on things, such as reading the newspaper or watching television?", choices1],
        [
            "Moving or speaking so slowly that other people could have noticed? Or so fidgety or restless that you have been moving a lot more than usual?",
            choices1],
        ["Thoughts that you would be better off dead, or thoughts of hurting yourself in some way?", choices1],
        [
            "How difficult have these problems made it for you to do your work, take care of things at home, or get along with other people?",
            choices2]
    ]

    return render(request, 'application/survey.html', {'title': 'PHQ-9',
                                                       'introduction': introduction,
                                                       'questions': questions})


def process_phq9(request, results):
    phq9 = PHQ9()
    # returns dictionary {diag : bool, change treat : bool, suicide : bool, score : int}
    dic = phq9.phq9_evaluation(results)
    phq9 = phq9_db.objects.create(question_1=results.get(str(1))[0],
                                  question_2=results.get(str(2))[0],
                                  question_3=results.get(str(3))[0],
                                  question_4=results.get(str(4))[0],
                                  question_5=results.get(str(5))[0],
                                  question_6=results.get(str(6))[0],
                                  question_7=results.get(str(7))[0],
                                  question_8=results.get(str(8))[0],
                                  question_9=results.get(str(9))[0],
                                  question_10=results.get(str(10))[0],
                                  diagnosis=dic.get("diagnosis"),
                                  severity_score=dic.get("severity_score"),
                                  change_treatment=dic.get("change_treatment"),
                                  suicide_risk=dic.get("suicide_risk")
                                  )

    request.session['survey_id'] = phq9.id

    return render(request, 'application/survey-complete.html', {'title': "Survey Complete"})


def get_mdq(request):
    introduction = "Has there ever been a period of time when you were not your usual self and..."
    choices1 = ["No", "Yes"]
    choices2 = ["No Problems", "Minor Problem", "Moderate Problem", "Serious Problem"]
    questions = [
        [
            "...you felt so good or so hyper that other people thought you were not your normal self or you were so hyper that you got into trouble?",
            choices1],
        ["...you were so irritable that you shouted at people or started fights or arguments?", choices1],
        ["...you felt much more self-confident than usual?", choices1],
        ["...you got much less sleep than usual and found that you didn't really miss it?", choices1],
        ["...you were more talkative or spoke much faster than usual?", choices1],
        ["...thoughts raced through your head or you couldn't slow your mind down?", choices1],
        ["...you were so easily distracted by things around you that you had trouble concentrating or staying on track",
         choices1],
        ["...you had more energy than normal?", choices1],
        ["...you were much more active or did many more things than usual?", choices1],
        [
            "...you were much more social or outgoing that usual, for example you telephoned friends in the middle of the night?",
            choices1],
        ["...you were much more interested in sex than usual?", choices1],
        [
            "...you did things that were unusual for you or that other people might have thought were excessive, foolish or risky?",
            choices1],
        ["...spending money got you or your family in trouble?", choices1],
        [
            "If you checked YES to more than one of the above, have several of these ever happened during the same period of time?",
            choices1],
        [
            "How much of a problem did any of these cause you - like being unable to work; having family, money or legal troubles; getting into arguments or fights?",
            choices2],
    ]

    return render(request, 'application/survey.html', {'title': 'MDQ',
                                                       'introduction': introduction,
                                                       'questions': questions})


def process_mdq(request, results):
    mdq = MDQ()

    # TODO process mdq results and get diagnosis
    diagnosis = True

    mdq = mdq_db.objects.create(question_1=results.get(str(1))[0],
                                question_2=results.get(str(2))[0],
                                question_3=results.get(str(3))[0],
                                question_4=results.get(str(4))[0],
                                question_5=results.get(str(5))[0],
                                question_6=results.get(str(6))[0],
                                question_7=results.get(str(7))[0],
                                question_8=results.get(str(8))[0],
                                question_9=results.get(str(9))[0],
                                question_10=results.get(str(10))[0],
                                question_11=results.get(str(11))[0],
                                question_12=results.get(str(12))[0],
                                question_13=results.get(str(13))[0],
                                question_14=results.get(str(14))[0],
                                question_15=results.get(str(15))[0],
                                diagnosis=diagnosis,
                                )

    request.session['survey_id'] = mdq.id

    return render(request, 'application/survey-complete.html', {'title': "Survey Complete"})


@login_required  # If user is not logged in, they are redirected to the login page.
def medications(request):
    return render(request, 'application/medications.html', {'title': 'Medications', 'medications': Medication.objects.all()})

class CreatePatientForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    # datepicker sourced from https://stackoverflow.com/questions/31548373/django-1-8-django-crispy-forms-is-there-a-simple-easy-way-of-implementing-a
    dob = forms.DateField(widget=forms.TextInput(attrs={'type':'date'}))
    address = forms.CharField()
    email = forms.EmailField()
    phone = forms.CharField()
    current_step = forms.ModelChoiceField(Step.objects)
    next_visit = forms.DateTimeField(initial=datetime.datetime.now(),
                                     widget=forms.DateTimeInput(format='%m/%d/%Y %H:%M'),
                                     input_formats=('%m/%d/%Y %H:%M',))
    notes = forms.CharField()

    class Meta:
        model = Patient
        fields = ['first_name', 'last_name', 'dob', 'address', 'email', 'phone', 'current_step',
                  'next_visit', 'notes']


@login_required  # If user is not logged in, they are redirected to the login page.
def new_patient(request):
    if request.method == 'POST':
        new_patient_form = CreatePatientForm(request.POST)
        if new_patient_form:
            new_patient_form.save()
            messages.success(request, 'Patient created.')
            return redirect('patients')
    else:
        new_patient_form = CreatePatientForm()
    return render(request, 'application/new-patient.html', {'new_patient_form': new_patient_form})


@login_required  # If user is not logged in, they are redirected to the login page.
def treatment_overview(request):
    return render(request, 'application/treatment-overview.html', {'title': 'Treatment Overview'})

@login_required  # If user is not logged in, they are redirected to the login page.
def bipolar_treatment_overview(request):
    return render(request, 'application/bipolar-treatment-overview.html', {'title': 'Bipolar Treatment Overview'})


@login_required
def algorithm(request):
    alg = request.GET.get('algorithm', None)
    if alg:
        request.session['algorithm'] = alg
    elif request.session.get('algorithm', None):
        alg = request.session['algorithm']
    else:
        alg = "Depression"
    raw_steps = serializers.serialize('python', Treatment.objects.get(name=alg).steps.all().order_by('id'))
    steps = {}
    for step in raw_steps:
        id = step['pk']
        step = step['fields']
        steps[id] = step
    steps = json.dumps(steps)

    if request.method == 'POST':
        # Set Step's coordinates in the database
        new_steps = json.loads(request.POST['steps'])
        for step in Treatment.objects.get(name=alg).steps.all().order_by('id'):
            new_step = new_steps[str(step.id)]
            step.x = new_step['x']
            step.y = new_step['y']
            step.save()

        return redirect('algorithm')
    else:
        return render(request, 'application/algorithm.html', {'title': 'Algorithm', 'algorithm': alg, 'steps': steps})


def pocket_guide(request):
    return render(request, 'application/pocket_guide.pdf', {'title': 'Pocket Guide'})


def bug_report(request):
    if request.method == 'POST':
        if os.getenv('GAE_APPLICATION', None):
            report = request.POST['report']
            key = get_datastore_key('GITHUB_KEY')
            g = Github(key)
            try:
                repo = g.get_repo("Brick7Face/psychiatric-guide-app")
                issue = repo.create_issue(
                    "User Generated Report: " + str(datetime.datetime.now()),
                    body=report
                )
                messages.success(request, 'Bug report submitted.')
            except:
                messages.error(request, 'An error occurred, please try again later.')
        else:
            messages.error(request, 'Bugs can only be reported when running on app engine')
        return redirect('bug_report')
    else:
        return render(request, 'application/bug-report.html', {'title': 'Report a Bug'})


def get_datastore_key(name):
    client = datastore.Client()
    key = client.key('key', name)
    return client.get(key)['value']


@login_required  # If user is not logged in, they are redirected to the login page.
def edit_patient(request, id): # View to edit the patient information
    patient = Patient.objects.get(pk=id)    #Gets the patient database field
    if request.method == 'POST':
        edit_patient_form = CreatePatientForm(request.POST, instance=patient)
        if edit_patient_form:
            edit_patient_form.save()
            messages.success(request, 'Patient edited.')
            return redirect('patients')
    else:
        edit_patient_form = CreatePatientForm(instance=patient) # Form receives the patients data base info and populates the form
    return render(request, 'application/edit-patient.html', {'edit_patient_form': edit_patient_form})


def memes(request):
    client_id = request.session.get('reddit_client_id', None)
    client_secret = request.session.get('reddit_client_secret', None)
    password = request.session.get('reddit_client_password', None)

    if not client_id:
        client_id = get_datastore_key('REDDIT_CLIENT_ID')
    if not client_secret:
        client_secret = get_datastore_key('REDDIT_CLIENT_SECRET')
    if not password:
        password = get_datastore_key('REDDIT_PASSWORD')

    reddit = praw.Reddit(user_agent='psychiatric-memes',
                         client_id=client_id,
                         client_secret=client_secret,
                         username='psychiatric-memes',
                         password=password)

    request.session['reddit_client_id'] = client_id
    request.session['reddit_client_secret'] = client_secret
    request.session['reddit_password'] = password

    subreddit = reddit.subreddit('memes')
    while True:
        post = subreddit.random()
        if post.selftext == '' and re.search(r"(?:([^:/?#]+):)?(?://([^/?#]*))?([^?#]*\.(?:jpg|gif|png))(?:\?([^#]*))?(?:#(.*))?", post.url):
            break
    return render(request, 'application/memes.html', {'title': 'Memes', 'heading': post.title, 'body': post.url, 'link': post.permalink})