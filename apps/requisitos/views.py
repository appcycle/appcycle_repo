import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django_filters.views import FilterView
from apps.requisitos.filters import RequisitoFilter
from apps.requisitos.forms import CadastrarRequisitos
from apps.requisitos.models import Requisito, PrioridadeRequisito, StatusRequisito, RiscoRequisito


@method_decorator(login_required, name='dispatch')
class RequisitoCreate(CreateView):
    model = Requisito
    form_class = CadastrarRequisitos

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(RequisitoCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class RequisitoList(ListView):
    paginate_by = 5
    model = Requisito
    ordering = ['-id']




#    def get_queryset(self):
#        usuarioLogado = self.request.user
#        return Requisito.objects.filter(user=usuarioLogado)


@method_decorator(login_required, name='dispatch')
class RequisitoDelete(DeleteView):
    model = Requisito
    success_url = reverse_lazy('search_results')


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
              'urlRepositorio',
              'urlJira',
              'requisitosImpactados',
              'estoriaUsuario',
              'regrasNegocio',
              'documento'
              ]


@method_decorator(login_required, name='dispatch')
class DetalheRequisitoView(DetailView):
    model = Requisito


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
    ordering = ['-id']


@method_decorator(login_required, name='dispatch')
class PrioridadeRequisitoView(UpdateView):
        model = PrioridadeRequisito
        fields = ['prioridade_requisito']


@method_decorator(login_required, name='dispatch')
class PrioridadeRequisitoDelete(DeleteView):
    model = PrioridadeRequisito
    success_url = reverse_lazy('visualizarprioridaderequisito')


@method_decorator(login_required, name='dispatch')
class StatusRequisitoCreate(CreateView):
    model = StatusRequisito
    fields = ['status_requisito']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(StatusRequisitoCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class StatusRequisitoList(ListView):
    paginate_by = 10
    model = StatusRequisito
    ordering = ['-id']


@method_decorator(login_required, name='dispatch')
class StatusRequisitoDelete(DeleteView):
    model = StatusRequisito
    success_url = reverse_lazy('visualizarstatusrequisito')


@method_decorator(login_required, name='dispatch')
class StatusRequisitoView(UpdateView):
        model = StatusRequisito
        fields = ['status_requisito']


@method_decorator(login_required, name='dispatch')
class RiscoRequisitoCreate(CreateView):
    model = RiscoRequisito
    fields = ['risco_requisito']

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(RiscoRequisitoCreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class RiscoRequisitoList(ListView):
    paginate_by = 10
    model = RiscoRequisito
    ordering = ['-id']



@method_decorator(login_required, name='dispatch')
class RiscoRequisitoView(UpdateView):
        model = RiscoRequisito
        fields = ['risco_requisito']



@method_decorator(login_required, name='dispatch')
class RiscoRequisitoDelete(DeleteView):
    model = RiscoRequisito
    success_url = reverse_lazy('visualizarriscorequisito')


@method_decorator(login_required, name='dispatch')
class SearchResultsListView(FilterView):
    paginate_by = 5
    model = Requisito
    filterset_class = RequisitoFilter # ADD YOUR filterset class
    ordering = ['-id']


@method_decorator(login_required, name='dispatch')
class ExportarCsvRequisito(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="requisitoscsv.csv"'

        registrorequisito = Requisito.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Codigo', 'Nome do Requisito', 'Criado Por', 'Projeto', 'Ponto Focal', 'Prioridade', 'Risco',
                         'Status', 'Story Points'])

        for registro in registrorequisito:
            writer.writerow([registro.codigo, registro.nomeRequisito, registro.user.first_name + ' ' + registro.user.last_name, registro.projeto, registro.ponto_focal,
                             registro.prioridade, registro.risco, registro.status, registro.storypoints])

        return response







