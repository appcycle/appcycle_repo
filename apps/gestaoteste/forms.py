from django.forms import ModelForm

from apps.gestaoteste.models import GestaoTeste
from apps.requisitos.models import Requisito


class GestaodeTesteForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(GestaodeTesteForm, self).__init__(*args, **kwargs)
        self.fields['requisito_associado'].queryset = Requisito.objects.filter(
             user=user)

    class Meta:
        model = GestaoTeste
        fields = [
            'nome_caso_teste',
            'codigo',
            'requisito_associado',
            'status',
            'prioridade',
            'caso_de_teste',
            'caso_de_teste_doc',
            'automatizado'
        ]
