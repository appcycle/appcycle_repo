import django_filters
import self

from apps.projeto.models import Projeto
from apps.requisitos.models import Requisito


class RequisitoFilter(django_filters.FilterSet):

    class Meta:
        model = Requisito
        fields = ['nomeRequisito', 'projeto']





