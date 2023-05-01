from django.contrib.auth.models import User
from django.forms import ModelForm
from apps.projeto.models import Projeto
from apps.requisitos.models import Requisito


class CadastrarRequisitos(ModelForm):

    class Meta:
        model = Requisito
        fields = ['codigo',
                  'nomeRequisito',
                  'responsavel',
                  'storypoints',
                  'projeto',
                  'prioridade',
                  'status',
                  'risco',
                  'urlRepositorio',
                  'urlJira',
                  'motivo',
                  'ponto_focal',
                  'requisitosImpactados',
                  'estoriaUsuario',
                  'regrasNegocio',
                  'documento']

