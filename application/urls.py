from django.urls import path
from django.contrib.auth import views as log_view # views for login/logout provided by django

from application import views

urlpatterns = [
    # path('', views.login, name='application-login'), # '' Directs to main /application page

    # Home page of entire site
    path('', log_view.LoginView.as_view(template_name='application/login.html'), name="login-view"),
    # login page at /login
    path('login/', log_view.LoginView.as_view(template_name='application/login.html'), name="login-view"),
    # Logout page at
    path('logout', log_view.LogoutView.as_view(template_name='application/global-html.html'), name="logout-view"),
    # survey page at survey/
    path('survey/', views.survey, name="survey-view")
]
