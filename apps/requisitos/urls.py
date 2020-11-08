from django.conf.urls import url
from django.urls import path

from . import views
from .views import (

    RequisitoCreate,
    RequisitoList,
    RequisitoDelete,
    RequisitoView
)

urlpatterns = [
     path('cadastrarrequisito/', RequisitoCreate.as_view(), name='cadastrarrequisito'),
     path('visualizarrequisito/', RequisitoList.as_view(), name='visualizarrequisito'),
     path('apagarrequisito/<int:pk>/', RequisitoDelete.as_view(), name='apagarrequisito'),
     path('editarrequisito/<int:pk>/', RequisitoView.as_view(), name='atualizarrequisito'),


]