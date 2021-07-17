import django_filters
from .models import Projeto

class ProjetoFilter(django_filters.FilterSet):
    nomeProjeto = django_filters.CharFilter(lookup_expr='icontains')
    nomeSprint = django_filters.CharFilter(lookup_expr='icontains')
    status = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Projeto
        fields = ['nomeProjeto', 'nomeSprint']