from django.urls import path
from .views import (
    CadastroCreate
)

urlpatterns = [
     path('cadastrar/', CadastroCreate.as_view(), name='cadastrar'),

]
