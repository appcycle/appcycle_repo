from django.urls import path

from apps.changelog.views import ChangelogList

urlpatterns = [
    path('changelog/', ChangelogList.as_view(), name='changelog')
]