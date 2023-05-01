from decimal import Decimal

from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.urls import reverse


class CadastroCliente(models.Model):
    nome_completo = models.CharField(max_length=70, verbose_name='Nome Completo: ', null=False, blank=False)
    cpf = models.CharField(max_length=20, verbose_name='CPF: ', null=False, blank=False)
    cargo = models.CharField(max_length=20, verbose_name='Cargo: ', null=False, blank=False)
    email = models.EmailField(max_length=30, verbose_name='E-mail: ', null=False, blank=False)
    telefone = models.CharField(max_length=40, verbose_name='Telefone (com DDD): ', null=False, blank=False)
    celular = models.CharField(max_length=40, verbose_name='Celular (com DDD): ', null=False, blank=False)
    nome_empresa = models.CharField(max_length=80, verbose_name='Nome da Empresa: ', null=False, blank=False)
    endereco = models.TextField(verbose_name='Endereço Completo da Empresa: ', null=False, blank=False)
    qtde_usuarios = models.PositiveIntegerField(verbose_name='Quantidade de usuários: ',
                                                validators=[MinValueValidator(1)],
                                                null=False, blank=False)



    def __str__(self):
        return self.nome_empresa

    def get_absolute_url(self):
        return reverse('sucesso')

