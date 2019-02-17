from django.urls import path
from django.contrib.auth import views as log_view  # views for login/logout provided by django
from . import views

urlpatterns = [
    path('', log_view.LoginView.as_view(template_name='application/login.html')),  # Home page of entire site
    path('login/', log_view.LoginView.as_view(template_name='application/login.html'), name='login-view'), # login page at /login
    path('logout/', views.logout_user, name="logout-view"),  # Logout page at
    path('create_user/', views.create_user, name='create-new-user'),  # Path for new user registration
    path('backend_home/', views.backend_home, name="backend-home"),  # Home page for logged in user
    path('documentation/', views.documentation, name="documentation"),  # Home page for logged in user
    path('survey/', views.survey, name="survey-view"),
    path('contact-bug/', views.contact_bug, name="contact-bug"),
    path('patient_home/', views.patient_home, name="patient-home"),
    path('phq9_results/', views.phq9_results, name="phq9-results"),
]
