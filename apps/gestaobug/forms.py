from django.forms import ModelForm

from apps.gestaobug.models import GestaoBug, SeveridadeBug, StatusBug


class GestaoBugForm(ModelForm):
    #def __init__(self, user, *args, **kwargs):
    #    super(GestaoBugForm, self).__init__(*args, **kwargs)
    #    self.fields['status_bug'].queryset = GestaoBug.objects.filter(
    #         user=user)

    class Meta:
        model = GestaoBug
        fields = [
            'codigo_bug',
            'nome_bug',
            'desenvolvedor_responsavel',
            'relator_bug',
            'ct_relacionado',
            'descricao_bug',
            'severidade_bug',
            'status_bug',
            'upload_bug'

        ]



class GestaoSeveridadeBugForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(GestaoSeveridadeBugForm, self).__init__(*args, **kwargs)
        self.fields['severidade_bug'].queryset = SeveridadeBug.objects.filter(
             user=user)

    class Meta:
        model = SeveridadeBug
        fields = [
            'severidade_bug'
            ]


class GestaoStatusBugForm(ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(GestaoStatusBugForm, self).__init__(*args, **kwargs)
        self.fields['status_bug'].queryset = SeveridadeBug.objects.filter(
             user=user)

    class Meta:
        model = StatusBug
        fields = [
            'status_bug'
            ]
