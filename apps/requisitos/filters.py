import django_filters
from apps.requisitos.models import Requisito


class RequisitoFilter(django_filters.FilterSet):

    class Meta:
        model = Requisito
        fields = ['codigo', 'nomeRequisito', 'projeto']






