from django.shortcuts import render
from django.views.generic import CreateView

from .models import CadastroCliente

class CadastroCreate(CreateView):
    model = CadastroCliente
    fields = ['nome_completo',
              'cpf',
              'telefone',
              'celular',
              'cargo',
              'email',
              'nome_empresa',
              'endereco',
              'qtde_usuarios'
             ]



def sucesso(request):
    return render(request, 'cadastro/sucesso.html')
