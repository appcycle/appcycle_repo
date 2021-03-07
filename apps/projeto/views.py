from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render
from django.template.context_processors import request
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from .models import Projeto, StatusProjeto
from ..requisitos.forms import CadastrarRequisitos


@method_decorator(login_required, name='dispatch')
class ProjetoCreate(SuccessMessageMixin, CreateView):
    model = Projeto
    success_url = '/projeto/cadastrarprojeto/'

    fields = ['nomeProjeto',
              'descricao',
              'dtInicio',
              'deadline',
              'nomeSprint',
              'status',
             ]


    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(ProjetoCreate, self).form_valid(form)


    def get_success_message(self, cleaned_data):
        print(cleaned_data)
        return "Projeto criado com sucesso!"


@method_decorator(login_required, name='dispatch')
class ProjetoList(ListView):
    paginate_by = 10
    model = Projeto

   # def get_queryset(self):
   #     usuarioLogado = self.request.user
   #     return Projeto.objects.filter(user=usuarioLogado)


@method_decorator(login_required, name='dispatch')
class ProjetoDelete(DeleteView):
    model = Projeto
    success_url = reverse_lazy('visualizarprojeto')


@method_decorator(login_required, name='dispatch')
class ProjetoView(UpdateView):
    model = Projeto
    fields = ['nomeProjeto', 'descricao', 'dtInicio', 'deadline', 'nomeSprint', 'status']


@method_decorator(login_required, name='dispatch')
class StatusProjetoCreate(CreateView):
    model = StatusProjeto
    fields = ['statusprojeto', ]

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(StatusProjetoCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class StatusProjetoList(ListView):
    paginate_by = 10
    model = StatusProjeto


@method_decorator(login_required, name='dispatch')
class StatusProjetoDelete(DeleteView):
    model = StatusProjeto
    success_url = reverse_lazy('visualizarstatusprojeto')


@method_decorator(login_required, name='dispatch')
class StatusProjetoView(UpdateView):
    model = StatusProjeto
    fields = ['statusprojeto',]


@method_decorator(login_required, name='dispatch')
class DetalheView(DetailView):
    model = Projeto
