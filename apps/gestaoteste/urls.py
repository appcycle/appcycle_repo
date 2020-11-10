from django.urls import path

from apps.gestaoteste.views import CTcreate, CTview, CTdelete, CTlist

urlpatterns = [
     path('cadastrarct/', CTcreate.as_view(), name='cadastrarct'),
     path('visualizarct/', CTlist.as_view(), name='visualizarct'),
     path('apagarct/<int:pk>/', CTdelete.as_view(), name='apagarct'),
     path('editarct/<int:pk>/', CTview.as_view(), name='atualizarct'),

]