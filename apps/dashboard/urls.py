from django.urls import re_path

from apps.dashboard.views import home, changelog

urlpatterns = [
     re_path('dashboard/', home, name='dashboard'),
     re_path('changelog/', changelog, name='changelog'),
]