from django.urls import include, re_path
from django.urls import path
from django_filters.views import FilterView

from .models import Projeto
from .views import (
    ProjetoCreate,
    ProjetoList,
    ProjetoDelete,
    ProjetoView,
    StatusProjetoCreate,
    StatusProjetoList,
    StatusProjetoDelete,
    StatusProjetoView, DetalheView, SearchResultsProjetoListView, ExportarCsvProjeto

)


urlpatterns = [
     path('cadastrarprojeto/', ProjetoCreate.as_view(), name='cadastrarprojeto'),
     path('visualizarprojeto/', ProjetoList.as_view(), name='visualizarprojeto'),
     path('apagarprojeto/<int:pk>/', ProjetoDelete.as_view(), name='apagarprojeto'),
     path('editarprojeto/<int:pk>/', ProjetoView.as_view(), name='atualizarprojeto'),
     path('cadastrarstatusprojeto/', StatusProjetoCreate.as_view(), name='cadastrarstatusprojeto'),
     path('visualizarstatusprojeto/', StatusProjetoList.as_view(), name='visualizarstatusprojeto'),
     path('apagarstatusprojeto/<int:pk>/', StatusProjetoDelete.as_view(), name='apagarstatusprojeto'),
     path('atualizarstatusprojeto/<int:pk>/', StatusProjetoView.as_view(), name='atualizarstatusprojeto'),
     path('detalheprojeto/<int:pk>/', DetalheView.as_view(), name='detalheprojeto'),
     path('search_projeto/', SearchResultsProjetoListView.as_view(), name='search_projeto'),
     path('exportarcsv_projeto/', ExportarCsvProjeto.as_view(), name='exportarcsv_projeto'),
]