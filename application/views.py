import datetime
import json
import os

from django.db.models import Model
from django.forms import Form
from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from django.core import serializers
from django.template.defaulttags import register
from django.views.generic import UpdateView

from application.models import Prescriber, Step, Patient
from application.models import Phq9 as phq9_db
from django import forms
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from application.questionnaire_evaluations import PHQ9

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
        new_user_form = CreateUser(request.POST)  # Form for creating a new user
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
    if request.method == 'POST':
        # take PHQ-9
        request.session['patient_id'] = request.POST['patient_id']
        return redirect('survey')
    else:
        patient_id = request.session["patient_id"]
        return render(request, 'application/patient-home.html',
                      {'title': 'Patient Home',
                       'patient': Patient.objects.get(id=patient_id),
                       'phq9s': phq9_db.objects.filter(patient_id=patient_id)})  # Renders login.html


@login_required  # If user is not logged in, they are redirected to the login page.
def phq9_results(request):
    print("TEST ", phq9_db.objects.last().diagnosis)
    dict = {'diagnosis': phq9_db.objects.last().diagnosis, 'change_treatment': phq9_db.objects.last().change_treatment,
            'suicide_risk': phq9_db.objects.last().suicide_risk,
            'severity_score': phq9_db.objects.last().severity_score}
    return render(request, 'application/phq9-results.html', dict)  # Renders login.html


@login_required
def phq9_results(request):
    if request.method == 'POST':
        # add phq-9 results to the patient
        patient_id = request.session['patient_id']
        phq9 = phq9_db.objects.get(id=request.session['phq9_id'])
        phq9.patient_id = patient_id
        phq9.save()
        return redirect('patient-home')
    else:
        dict = {'diagnosis': phq9_db.objects.last().diagnosis,
                'change_treatment': phq9_db.objects.last().change_treatment,
                'suicide_risk': phq9_db.objects.last().suicide_risk,
                'severity_score': phq9_db.objects.last().severity_score}
        return render(request, 'application/phq9-results.html', dict)  # Renders login.html


def documentation(request):
    return render(request, 'application/documentation.html', {'title': 'Documentation'})  # Renders login.html


@login_required  # If user is not logged in, they are redirected to the login page.
def survey(request):
    if request.method == 'POST':
        # TODO: calculate calculate and save results here
        results = dict(request.POST)

        results.pop('csrfmiddlewaretoken', '')
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

        request.session['phq9_id'] = phq9.id

        return render(request, 'application/survey-complete.html', {'title': "Survey Complete"})

    else:
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

        return render(request, 'application/survey.html', {'title': 'Survey',
                                                           'introduction': introduction,
                                                           'questions': questions})


@login_required  # If user is not logged in, they are redirected to the login page.
def medications(request):
    return render(request, 'application/medications.html', {'title': 'Medications'})


class CreatePatientForm(forms.ModelForm):
    first_name = forms.CharField()
    last_name = forms.CharField()
    dob = forms.DateField(initial=datetime.date.today,
                          widget=forms.DateInput(format='%m/%d/%Y'),
                          input_formats=('%m/%d/%Y',))
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


@login_required
def algorithm(request):
    raw_steps = serializers.serialize('python', Step.objects.all().order_by('id'))
    steps = {}
    for step in raw_steps:
        id = step['pk']
        step = step['fields']
        steps[id] = step
    steps = json.dumps(steps)
    return render(request, 'application/algorithm.html', {'title': 'Algorithm', 'steps': steps})


def pocket_guide(request):
    return render(request, 'application/pocket_guide.pdf', {'title': 'Pocket Guide'})


def bug_report(request):
    if request.method == 'POST':
        if os.getenv('GAE_APPLICATION', None):
            report = request.POST['report']
            key = get_datastore_key('GITHUB_KEY')
            print(key)
            g = Github(key)
            try:
                repo = g.get_repo("Brick7Face/psychiatric-guide-app")
                issue = repo.create_issue(
                    "User Generated Report: " + str(datetime.datetime.now()),
                    body=report
                )
                print(issue.html_url)
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
