import django_filters
from .models import GestaoBug

class BugFilter(django_filters.FilterSet):

    class Meta:
        model = GestaoBug
        fields = ['codigo_bug', 'nome_bug']