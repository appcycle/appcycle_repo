from django.contrib.auth.decorators import login_required
from django.http import request
from django.shortcuts import render
from django.urls import reverse_lazy

from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView

from apps.requisitos.filters import RequisitoFilter
from apps.requisitos.forms import CadastrarRequisitos
from apps.requisitos.models import Requisito, PrioridadeRequisito


@method_decorator(login_required, name='dispatch')
class RequisitoCreate(CreateView):
    model = Requisito
    form_class = CadastrarRequisitos

    def get_form_kwargs(self):
        kwargs = super(RequisitoCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(RequisitoCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class RequisitoList(ListView):
    paginate_by = 10
    model = Requisito

#    def get_queryset(self):
#        usuarioLogado = self.request.user
#        return Requisito.objects.filter(user=usuarioLogado)


@method_decorator(login_required, name='dispatch')
class RequisitoDelete(DeleteView):
    model = Requisito
    success_url = reverse_lazy('visualizarrequisito')


@method_decorator(login_required, name='dispatch')
class RequisitoView(UpdateView):
    model = Requisito
    fields = ['nomeRequisito',
              'responsavel',
              'storypoints',
              'codigo',
              'projeto',
              'prioridade',
              'risco',
              'motivo',
              'ponto_focal',
              'status',
              'requisitosImpactados',
              'estoriaUsuario',
              'regrasNegocio',
              'documento'
              ]



@method_decorator(login_required, name='dispatch')
class RequisitoCreate(CreateView):
    model = Requisito
    form_class = CadastrarRequisitos

    def get_form_kwargs(self):
        kwargs = super(RequisitoCreate, self).get_form_kwargs()
        kwargs.update({'user': self.request.user})
        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(RequisitoCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class PrioridadeRequisitoCreate(CreateView):
    model = PrioridadeRequisito
    fields = ['prioridade_requisito']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(PrioridadeRequisitoCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class PrioridadeRequisitoList(ListView):
    paginate_by = 10
    model = PrioridadeRequisito


@method_decorator(login_required, name='dispatch')
class PrioridadeRequisitoView(UpdateView):
        model = PrioridadeRequisito
        fields = ['prioridade_requisito']



@method_decorator(login_required, name='dispatch')
class PrioridadeRequisitoDelete(DeleteView):
    model = PrioridadeRequisito
    success_url = reverse_lazy('visualizarprioridaderequisito')
