from django.urls import path

from apps.gestaoteste.views import CTcreate, CTview

urlpatterns = [
     path('cadastrarct/', CTcreate.as_view(), name='cadastrarct'),
     path('visualizarct/', CTview.as_view(), name='visualizarct'),
    # path('apagarprojeto/<int:pk>/', ProjetoDelete.as_view(), name='apagarprojeto'),
    # path('editarprojeto/<int:pk>/', ProjetoView.as_view(), name='atualizarprojeto'),

]