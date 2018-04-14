from django.urls import path

from . import views
from triplanner.views import *

urlpatterns = [
    path('', views.home, name='home'),
]
