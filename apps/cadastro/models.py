from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Cadastro(models.Model):
    nomeCompleto = models.CharField(max_length=70, verbose_name='Nome Completo: ')
    cpf = models.CharField(max_length=20, verbose_name='CPF: ')
    cargo = models.CharField(max_length=20, verbose_name='Cargo: ')
    email = models.EmailField(max_length=30, verbose_name='E-mail: ')
    telefone = models.CharField(max_length=40, verbose_name='Telefone (com DDD): ')
    celular = models.CharField(max_length=40, verbose_name='Celular (com DDD): ')
    nomeEmpresa = models.CharField(max_length=80, verbose_name='Nome da Empresa: ')
    endereco = models.TextField(verbose_name='Endereço Completo da Empresa: ')


    def __str__(self):
        return self.nomeCompleto

    def get_absolute_url(self):
        return reverse('sucesso')

