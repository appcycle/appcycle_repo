from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField
from apps.projeto.models import Projeto


class Requisito (models.Model):
    nomeRequisito = models.CharField(max_length=30, verbose_name=('Nome do Requisito'))
    responsavel = models.CharField(max_length=30, verbose_name=('Responsável pelo Desenvolvimento'))
    código = models.CharField(max_length=20, verbose_name=('Código do Requisito'))
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT)
    prioridade = models.CharField(max_length=10, verbose_name=('Prioridade do Requisito'))
    risco = models.CharField(max_length=10, verbose_name=('Risco do Requisito'))
    motivo = models.CharField(max_length=20, verbose_name=('Motivo do Requisito'))
    status = models.CharField(max_length=20, verbose_name=('Status do Requisito'))
    requisitosImpactados = models.CharField(max_length=100, verbose_name=('Requisitos Impactados'))
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    estoriaUsuario = HTMLField()
    regrasNegocio = HTMLField()

    def __str__(self):
        return self.nomeRequisito

    def get_absolute_url(self):
        return reverse('visualizarRequisito')