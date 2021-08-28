from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.urls import reverse

from apps.requisitos.models import Requisito


class GestaoTeste(models.Model):
    nome_caso_teste = models.CharField(max_length=30, verbose_name=('Nome do Caso de Teste'))
    codigo = models.CharField(max_length=10, verbose_name=('Código do Caso de Teste'))
    requisito_associado = models.ForeignKey(Requisito, on_delete=models.PROTECT, null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    caso_de_teste_doc = models.FileField(upload_to='documentos', blank=True, null=True, verbose_name="Carregar Documento")
    objetivo_teste = models.CharField(max_length=50, verbose_name=('Objetivo do teste'), null=True, blank=True)
    status = models.CharField(max_length=15, verbose_name=('Status do Caso de Teste'), blank=True, null=True)
    caso_de_teste = models.TextField(verbose_name=('Caso de Teste'), blank=True, null=True)
    resultados_esperados = models.TextField(verbose_name=('Resultados esperados'), blank=True, null=True)
    prioridade = models.CharField(max_length=15, verbose_name=('Prioridade'), blank=True, null=True)
    automatizado = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_caso_teste

    def get_absolute_url(self):
        return reverse('search_ct')



