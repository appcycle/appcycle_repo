from django.shortcuts import render
from django.views.generic import CreateView

from .models import Cadastro

class CadastroCreate(CreateView):
    model = Cadastro
    fields = ['nomeCompleto',
              'cpf',
              'telefone',
              'celular',
              'cargo',
              'email',
              'nomeEmpresa',
              'endereco'

             ]

