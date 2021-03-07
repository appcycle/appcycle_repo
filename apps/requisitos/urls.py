from django.conf.urls import url
from django.urls import path

from . import views
from .views import (

    RequisitoCreate,
    RequisitoList,
    RequisitoDelete,
    RequisitoView,
    PrioridadeRequisitoCreate,
    PrioridadeRequisitoList,
    PrioridadeRequisitoView, PrioridadeRequisitoDelete, StatusRequisitoCreate, StatusRequisitoList,
    StatusRequisitoDelete, StatusRequisitoView, RiscoRequisitoCreate, RiscoRequisitoList, DetalheRequisitoView,

)

urlpatterns = [
     path('cadastrarrequisito/', RequisitoCreate.as_view(), name='cadastrarrequisito'),
     path('visualizarrequisito/', RequisitoList.as_view(), name='visualizarrequisito'),
     path('apagarrequisito/<int:pk>/', RequisitoDelete.as_view(), name='apagarrequisito'),
     path('editarrequisito/<int:pk>/', RequisitoView.as_view(), name='atualizarrequisito'),
     path('cadastrarprioridaderequisito/', PrioridadeRequisitoCreate.as_view(), name='cadastrarprioridaderequisito'),
     path('visualizarprioridaderequisito/', PrioridadeRequisitoList.as_view(), name='visualizarprioridaderequisito'),
     path('editarprioridaderequisito/<int:pk>/', PrioridadeRequisitoView.as_view(), name='atualizarprioridaderequisito'),
     path('apagarprioridaderequisito/<int:pk>/', PrioridadeRequisitoDelete.as_view(), name='apagarprioridaderequisito'),
     path('cadastrarstatudesrequisito/', StatusRequisitoCreate.as_view(), name='cadastrarstatusrequisito'),
     path('visualizarstatusderequisito/', StatusRequisitoList.as_view(), name='visualizarstatusrequisito'),
     path('apagarstatusderequisito/<int:pk>/', StatusRequisitoDelete.as_view(), name='apagarstatusrequisito'),
     path('editarstatusderequisito/<int:pk>/', StatusRequisitoView.as_view(), name='atualizarstatusrequisito'),
     path('cadastrarriscorequisito/', RiscoRequisitoCreate.as_view(), name='cadastrarriscorequisito'),
     path('visualizarriscorequisito/', RiscoRequisitoList.as_view(), name='visualizarriscorequisito'),
    path('detalherequisito/<int:pk>/', DetalheRequisitoView.as_view(), name='detalherequisito'),

]