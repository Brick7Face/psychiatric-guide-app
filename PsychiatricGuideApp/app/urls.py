from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'app_home'), # '' sets app home page
]