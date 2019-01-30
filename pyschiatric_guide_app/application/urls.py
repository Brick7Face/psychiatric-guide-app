from django.urls import path
from . import views

urlpatterns = [
    path('', views.login, name='application-login'), # '' Directs to main /application page


]
