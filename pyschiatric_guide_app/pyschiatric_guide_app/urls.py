"""pyschiatric_guide_app URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as log_view # views for login/logout provided by django

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('application.urls')),  # '' Sets home page
    path('application/', include('application.urls')),
    path('', log_view.LoginView.as_view(template_name='application/login.html'), name="login-view"), # Home page of entire site
    path('login/', log_view.LoginView.as_view(template_name='application/login.html'), name="login-view"), # login page at /login
    path('logout', log_view.LogoutView.as_view(template_name='application/global-html.html'), name="logout-view") # Logout page at
]
