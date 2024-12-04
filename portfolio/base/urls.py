from django.contrib import admin
from django.urls import path

from portfolio.base import views

app_name = 'base'

urlpatterns = [
    path('', views.home, name='home'),
]
