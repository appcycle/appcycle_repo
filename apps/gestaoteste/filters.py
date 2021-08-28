import django_filters
from .models import GestaoTeste

class CTFilter(django_filters.FilterSet):

    class Meta:
        model = GestaoTeste
        fields = ['codigo', 'nome_caso_teste']