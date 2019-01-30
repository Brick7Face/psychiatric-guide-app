from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name = 'user_home'), # '' sets user home page
]