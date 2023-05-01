from django.urls import path

from apps.dashboard.views import home, changelog

urlpatterns = [
     path('dashboard/', home, name='dashboard'),
     path('changelog/', changelog, name='changelog'),




]