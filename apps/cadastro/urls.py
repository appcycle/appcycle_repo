from django.urls import path
from .views import (
    CadastroCreate, sucesso
)

urlpatterns = [
     path('cadastrar/', CadastroCreate.as_view(), name='cadastrar'),
     path('sucesso/', sucesso, name='sucesso'),

]
