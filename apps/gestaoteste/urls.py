from django.urls import path

from apps.gestaoteste.views import CTcreate, CTview, CTdelete, CTlist, CTDetalheView, SearchResultCTListView, \
     ExportarCsvGestaoTeste

urlpatterns = [
     path('cadastrarct/', CTcreate.as_view(), name='cadastrarct'),
     path('visualizarct/', CTlist.as_view(), name='visualizarct'),
     path('apagarct/<int:pk>/', CTdelete.as_view(), name='apagarct'),
     path('editarct/<int:pk>/', CTview.as_view(), name='atualizarct'),
     path('detalhect/<int:pk>/', CTDetalheView.as_view(), name='detalhect'),
     path('search_ct/', SearchResultCTListView.as_view(), name='search_ct'),
     path('exportarcsv_ct/', ExportarCsvGestaoTeste.as_view(), name='exportarcsv_ct'),

]