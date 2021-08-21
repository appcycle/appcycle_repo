from django.urls import path


from apps.gestaobug.views import (
    BGseveridade,
    BGlistseveridade,
    BGapagarSeveridade,
    BGatualizarSeveridade,
    BGstatus,
    BGliststatus,
    BGapagarStatus,
    BGatualizarStatus,
    BGcreate,
    BGlist,
    BGapagar, BGatualizar, BGDetalheView, SearchResultsBugListView

)

urlpatterns = [
    path('cadastrarseveridadebug/', BGseveridade.as_view(), name='cadastrarseveridadebug'),
    path('visualizarseveridadebug/', BGlistseveridade.as_view(), name='visualizarseveridadebug'),
    path('apagarseveridadebug/<int:pk>/', BGapagarSeveridade.as_view(), name='apagarseveridadebug'),
    path('atualizarseveridadebug/<int:pk>/', BGatualizarSeveridade.as_view(), name='atualizarseveridadebug'),
    path('cadastrarstatusbug/', BGstatus.as_view(), name='cadastrarstatusbug'),
    path('visualizarstatusbug/', BGliststatus.as_view(), name='visualizarstatusbug'),
    path('apagarstatusbug/<int:pk>/', BGapagarStatus.as_view(), name='apagarstatusbug'),
    path('atualizarstatusbug/<int:pk>/', BGatualizarStatus.as_view(), name='atualizarstatusbug'),
    path('cadastrarbug/', BGcreate.as_view(), name='cadastrarbug'),
    path('visualizarbug/', BGlist.as_view(), name='visualizarbug'),
    path('apagarbug/<int:pk>', BGapagar.as_view(), name='apagarbug'),
    path('atualizarbug/<int:pk>', BGatualizar.as_view(), name='atualizarbug'),
    path('detalhebug/<int:pk>', BGDetalheView.as_view(), name='detalhebug'),
    path('search_bug/', SearchResultsBugListView.as_view(), name='search_bug'),
]