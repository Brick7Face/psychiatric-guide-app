from django.shortcuts import redirect, render
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.models import User
from application.models import Prescriber
from django import forms
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout

# Create your views here.


def login(request):
    return render(request, 'application/login.html', {'title': 'Login'})  # Renders login.html


def logout_user(request):
    logout(request) # Built in django logout function
    return redirect('login-view')  # Logs user out and redirects to login page


# Create user code helped from Youtube series by Cory Schafer: https://www.youtube.com/watch?v=UmljXZIypDc&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p
@login_required # If user is not logged in, they are redirected to the login page.
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


def backend_home(request):
    return render(request, 'application/backend-home.html', {'title': 'Home'})  # Renders login.html


def documentation(request):
    return render(request, 'application/documentation.html', {'title': 'Documentation'})  # Renders login.html

def contact_bug(request):
    return render(request, 'application/contact-bug.html', {'title': 'Contact Us / Report a Bug'})