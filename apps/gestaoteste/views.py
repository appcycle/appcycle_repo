import csv

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView, ListView, DeleteView, UpdateView, DetailView
from django_filters.views import FilterView

from apps.gestaoteste.filters import CTFilter
from apps.gestaoteste.forms import GestaodeTesteForm
from apps.gestaoteste.models import GestaoTeste


@method_decorator(login_required, name='dispatch')
class CTcreate (CreateView):
    model = GestaoTeste
    form_class = GestaodeTesteForm

#    def get_form_kwargs(self):
#        kwargs = super(CTcreate, self).get_form_kwargs()
#        kwargs.update({'user': self.request.user})
#        return kwargs

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(CTcreate, self).form_valid(form)


@method_decorator(login_required, name='dispatch')
class CTlist(ListView):
    paginate_by = 10
    model = GestaoTeste
    ordering = ['-id']

  #  def get_queryset(self):
  #      usuarioLogado = self.request.user
  #      return GestaoTeste.objects.filter(user=usuarioLogado)


@method_decorator(login_required, name='dispatch')
class CTdelete(DeleteView):
    model = GestaoTeste
    success_url = reverse_lazy('search_ct')



@method_decorator(login_required, name='dispatch')
class CTview(UpdateView):
    model = GestaoTeste
    fields = [
            'nome_caso_teste',
            'codigo',
            'requisito_associado',
            'status',
            'prioridade',
            'objetivo_teste',
            'caso_de_teste',
            'resultados_esperados',
            'caso_de_teste_doc',
            'automatizado'
            ]



@method_decorator(login_required, name='dispatch')
class CTDetalheView(DetailView):
    model = GestaoTeste


@method_decorator(login_required, name='dispatch')
class SearchResultCTListView(FilterView):
    paginate_by = 5
    model = GestaoTeste
    filterset_class = CTFilter # ADD YOUR filterset class
    ordering = ['-id']


@method_decorator(login_required, name='dispatch')
class ExportarCsvGestaoTeste(View):
    def get(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="gestaotestecsv.csv"'

        registroteste = GestaoTeste.objects.all()

        writer = csv.writer(response)
        writer.writerow(['Código', 'Nome do Caso de Teste', 'Requisito Associado', 'Criado por', 'Status',
                         'Prioridade', 'Automatizado'])

        for registro in registroteste:
            writer.writerow([registro.codigo, registro.nome_caso_teste, registro.requisito_associado, registro.user.first_name + ' ' + registro.user.last_name ,
                             registro.status, registro.prioridade, registro.automatizado])

        return response