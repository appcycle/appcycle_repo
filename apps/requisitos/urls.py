from django.urls import path
from .views import (

    RequisitoCreate,
    RequisitoList
)

urlpatterns = [
     path('cadastrarRequisito/', RequisitoCreate.as_view(), name='cadastrarRequisito'),
     path('visualizarRequisito/', RequisitoList.as_view(), name='visualizarRequisito'),
   #  path('apagarProjeto/<int:pk>/', ProjetoDelete.as_view(), name='apagarProjeto'),
   # path('editarProjeto/<int:pk>/', ProjetoView.as_view(), name='atualizarProjeto'),

]