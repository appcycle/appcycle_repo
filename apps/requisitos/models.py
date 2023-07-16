from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from apps.projeto.models import Projeto


class PrioridadeRequisito(models.Model):
    prioridade_requisito = models.CharField(max_length=20, verbose_name=('Prioridade do Requisito'), blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.prioridade_requisito

    def get_absolute_url(self):
        return reverse('visualizarprioridaderequisito')


class StatusRequisito(models.Model):
    status_requisito = models.CharField(max_length=20, verbose_name=('Status do Requisito'), blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.status_requisito

    def get_absolute_url(self):
        return reverse('visualizarstatusrequisito')


class RiscoRequisito(models.Model):
    risco_requisito = models.CharField(max_length=20, verbose_name=('Risco do Requisito'), blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.risco_requisito

    def get_absolute_url(self):
        return reverse('visualizarriscorequisito')


class Requisito (models.Model):
    nomeRequisito = models.CharField(max_length=30, verbose_name=('Nome do Requisito'))
    responsavel = models.CharField(max_length=30, verbose_name=('Responsável pelo Desenvolvimento'), null=True, blank=True)
    codigo = models.CharField(max_length=20, verbose_name=('Código do Requisito'))
    projeto = models.ForeignKey(Projeto, on_delete=models.PROTECT)
    ponto_focal = models.CharField(max_length=20, verbose_name=('Ponto Focal'), null=True, blank=True)
    prioridade = models.ForeignKey(PrioridadeRequisito, on_delete=models.PROTECT)
    risco = models.ForeignKey(RiscoRequisito, on_delete=models.PROTECT)
    motivo = models.CharField(max_length=100, verbose_name=('Motivo do Requisito'), null=True, blank=True)
    status = models.ForeignKey(StatusRequisito, on_delete=models.PROTECT)
    urlRepositorio = models.URLField(verbose_name=('URL no Repositório'), null=True, blank=True)
    urlJira = models.URLField(verbose_name=('URL no JIRA'), null=True, blank=True)
    storypoints = models.CharField(max_length=3, verbose_name=('Story Points'), null=True, blank=True)
    requisitosImpactados = models.TextField(verbose_name=('Requisitos Impactados'), null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    documento = models.FileField(upload_to='documentos', null=True, blank=True)
    estoriaUsuario = models.TextField(verbose_name='Estória do Usuário', null=True, blank=True)
    regrasNegocio = models.TextField(verbose_name='Regras de Negócios', null=True, blank=True)

    def __str__(self):
        return self.nomeRequisito

    def get_absolute_url(self):
        return reverse('search_results')