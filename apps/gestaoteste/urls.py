from django.urls import path

from apps.gestaoteste.views import CTcreate

urlpatterns = [
     path('cadastrarct/', CTcreate.as_view(), name='cadastrarct'),
     #path('visualizarprojeto/', ProjetoList.as_view(), name='visualizarprojeto'),
    # path('apagarprojeto/<int:pk>/', ProjetoDelete.as_view(), name='apagarprojeto'),
    # path('editarprojeto/<int:pk>/', ProjetoView.as_view(), name='atualizarprojeto'),

]