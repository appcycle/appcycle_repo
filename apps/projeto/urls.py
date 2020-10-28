from django.urls import path
from .views import (
    ProjetoCreate,
    ProjetoList,
    ProjetoDelete,
    ProjetoView
)

urlpatterns = [
     path('cadastrarProjeto/', ProjetoCreate.as_view(), name='cadastrarProjeto'),
     path('visualizarProjeto/', ProjetoList.as_view(), name='visualizarProjeto'),
     path('apagarProjeto/<int:pk>/', ProjetoDelete.as_view(), name='apagarProjeto'),
    path('editarProjeto/<int:pk>/', ProjetoView.as_view(), name='atualizarProjeto'),

]