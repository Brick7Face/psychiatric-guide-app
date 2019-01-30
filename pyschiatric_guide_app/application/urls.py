from django.urls import path
from django.contrib.auth import views as log_view # views for login/logout provided by django


urlpatterns = [
    # path('', views.login, name='application-login'), # '' Directs to main /application page
    path('', log_view.LoginView.as_view(template_name='application/login.html'), name="login-view"), # Home page of entire site
    path('login/', log_view.LoginView.as_view(template_name='application/login.html'), name="login-view"), # login page at /login
    path('logout', log_view.LogoutView.as_view(template_name='application/global-html.html'), name="logout-view") # Logout page at

]
