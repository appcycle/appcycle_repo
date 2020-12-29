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
    PrioridadeRequisitoView, PrioridadeRequisitoDelete,

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
]