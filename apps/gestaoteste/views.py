from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.generic import CreateView

from apps.gestaoteste.models import GestaoTeste


@method_decorator(login_required, name='dispatch')
class CTcreate (CreateView):
    model = GestaoTeste
    fields = ['nome_caso_teste',
              'codigo',
              'requisito_associado',
              'status',
              'prioridade',
              'caso_de_teste',
              'caso_de_teste_doc',
              'automatizado'
             ]

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(CTcreate, self).form_valid(form)
