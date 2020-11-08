from django.urls import path
from .views import (
    ProjetoCreate,
    ProjetoList,
    ProjetoDelete,
    ProjetoView
)

urlpatterns = [
     path('cadastrarprojeto/', ProjetoCreate.as_view(), name='cadastrarprojeto'),
     path('visualizarprojeto/', ProjetoList.as_view(), name='visualizarprojeto'),
     path('apagarprojeto/<int:pk>/', ProjetoDelete.as_view(), name='apagarprojeto'),
     path('editarprojeto/<int:pk>/', ProjetoView.as_view(), name='atualizarprojeto'),

]