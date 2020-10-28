from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView
from .models import Projeto


@method_decorator(login_required, name='dispatch')
class ProjetoCreate(CreateView):
    model = Projeto
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



@method_decorator(login_required, name='dispatch')
class ProjetoList(ListView):
    paginate_by = 10
    model = Projeto

    def get_queryset(self):
        usuarioLogado = self.request.user
        return Projeto.objects.filter(user=usuarioLogado)


@method_decorator(login_required, name='dispatch')
class ProjetoDelete(DeleteView):
    model = Projeto
    success_url = reverse_lazy('visualizarProjeto')


@method_decorator(login_required, name='dispatch')
class ProjetoView(UpdateView):
    model = Projeto
    fields = ['nomeProjeto', 'descricao', 'dtInicio', 'deadline', 'nomeSprint', 'status']



