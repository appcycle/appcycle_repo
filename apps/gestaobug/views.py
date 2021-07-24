from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView

from apps.gestaobug.forms import GestaoBugForm, GestaoSeveridadeBugForm, GestaoStatusBugForm
from apps.gestaobug.models import GestaoBug, SeveridadeBug, StatusBug


@method_decorator(login_required, name='dispatch')
class BGseveridade (CreateView):
    model = SeveridadeBug
    form_class = GestaoSeveridadeBugForm


   # def get_form_kwargs(self):
   #     kwargs = super(BGseveridade, self).get_form_kwargs()
   #     kwargs.update({'user': self.request.user})
   #     return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(BGseveridade, self).form_valid(form)



@method_decorator(login_required, name='dispatch')
class BGlistseveridade(ListView):
    paginate_by = 10
    model = SeveridadeBug
    ordering = ['-id']

   # def get_queryset(self):
   #     usuarioLogado = self.request.user
   #     return SeveridadeBug.objects.filter(user=usuarioLogado)



@method_decorator(login_required, name='dispatch')
class BGapagarSeveridade(DeleteView):
    model = SeveridadeBug
    success_url = reverse_lazy('visualizarseveridadebug')


@method_decorator(login_required, name='dispatch')
class BGatualizarSeveridade(UpdateView):
    model = SeveridadeBug
    fields = ['severidade_bug']


@method_decorator(login_required, name='dispatch')
class BGstatus (CreateView):
    model = StatusBug
    form_class = GestaoStatusBugForm

    #def get_form_kwargs(self):
    #    kwargs = super(BGstatus, self).get_form_kwargs()
    #    kwargs.update({'user': self.request.user})
    #    return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(BGstatus, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class BGliststatus(ListView):
    paginate_by = 10
    model = StatusBug

   # def get_queryset(self):
   #     usuarioLogado = self.request.user
   #     return StatusBug.objects.filter(user=usuarioLogado)


@method_decorator(login_required, name='dispatch')
class BGapagarStatus(DeleteView):
    model = StatusBug
    success_url = reverse_lazy('visualizarstatusbug')


@method_decorator(login_required, name='dispatch')
class BGatualizarStatus(UpdateView):
    model = StatusBug
    fields = ['status_bug']


@method_decorator(login_required, name='dispatch')
class BGcreate (CreateView):
    model = GestaoBug
    form_class = GestaoBugForm

   # def get_form_kwargs(self):
   #     kwargs = super(BGcreate, self).get_form_kwargs()
   #     kwargs.update({'user': self.request.user})
   #     return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(BGcreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class BGlist (ListView):
    model = GestaoBug
    form_class = GestaoBugForm
    paginate_by = 10
    model = GestaoBug
    ordering = ['-id']

   # def get_queryset(self):
   #     usuarioLogado = self.request.user
   #     return GestaoBug.objects.filter(user=usuarioLogado)


@method_decorator(login_required, name='dispatch')
class BGapagar(DeleteView):
    model = GestaoBug
    success_url = reverse_lazy('visualizarbug')


@method_decorator(login_required, name='dispatch')
class BGatualizar(UpdateView):
    model = GestaoBug
    fields = ['codigo_bug',
    'nome_bug',
    'relator_bug',
    'ct_relacionado',
    'descricao_bug',
    'upload_bug',
    'severidade_bug',
    'status_bug'
                ]



@method_decorator(login_required, name='dispatch')
class BGDetalheView(DetailView):
    model = GestaoBug
