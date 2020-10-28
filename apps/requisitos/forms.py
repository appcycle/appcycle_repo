from django.contrib.auth.models import User
from django.forms import ModelForm
from apps.projeto.models import Projeto
from apps.requisitos.models import Requisito


class CadastrarRequisitos(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(CadastrarRequisitos, self).__init__(*args, **kwargs)
        self.fields['projeto'].queryset = Projeto.objects.filter(
             user=user)

    class Meta:
        model = Requisito
        fields = ['nomeRequisito',
                  'responsavel',
                  'código',
                  'projeto',
                  'prioridade',
                  'status',
                  'risco',
                  'motivo',
                  'requisitosImpactados',
                  'estoriaUsuario',
                  'regrasNegocio']

